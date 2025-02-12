import json
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import List

from src.env import env
from src.logger import logger


class BaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def read(self) -> List[any]:
        raise NotImplementedError

    @abstractmethod
    def insert_many(self, ids: List[int]) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert(self, id: int) -> None:
        raise NotImplementedError


class Repository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._filepath = Path(env.DATA_FILE_PATH)

        with open(self._filepath, encoding="utf-8", mode="r") as data_file:
            try:
                data = json.loads(data_file.read())
            except json.decoder.JSONDecodeError as e:
                logger.warning(e)
                data = {"users": []}

        self.data = data

    def read(self):
        return self.data

    def insert_many(self, ids: List[int]) -> None:
        raise NotImplementedError

    def insert(self, username: str) -> None:
        if username in self.data["users"]:
            logger.info("user already exists")
            return

        self.data["users"].append(username)

        with open(str(env.DATA_FILE_PATH), encoding="utf-8", mode="w+") as data_file:
            json.dump(self.data, data_file, ensure_ascii=False, indent=4)


repository = Repository()
