import json
from pathlib import Path

from src.database.BaseRepository import BaseRepository
from src.env import env
from src.logger import logger


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._filepath = Path(env.DATA_FILE_PATH)

        if not self._filepath.exists():
            self._filepath.touch()

    def read(self) -> dict[str, list[str]]:
        users: list[str] = []

        with open(self._filepath, encoding="utf-8", mode="r") as data_file:
            try:
                users = json.loads(data_file.read())["users"]
            except json.decoder.JSONDecodeError as e:
                logger.warning(e)

        return {
            "users": users,
        }

    def insert(self, username: str) -> None:
        users = self.read()["users"]

        if username in users:
            logger.info("user already exists")
            return

        users.append(username)

        new_data = {"users": users}

        with open(str(env.DATA_FILE_PATH), encoding="utf-8", mode="w") as data_file:
            json.dump(new_data, data_file, ensure_ascii=False, indent=4)
