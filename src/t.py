from typing import Any, Optional

from pydantic import BaseModel, PositiveInt, SecretStr, StrictBool, StrictStr


class EnvModel(BaseModel):
    DEBUG: bool
    PORT: PositiveInt
    # DATABASE_URL: PostgresDsn
    DATA_FILE_PATH: StrictStr
    SECRET_KEY: SecretStr
    JWT_ACCESS_TOKEN_EXPIRES: PositiveInt


class CheckModel(BaseModel):
    name: StrictStr
    healthy: StrictBool
    data: Optional[dict[str, Any]] = None


class HealthResponseModel(BaseModel):
    healthy: StrictBool
    checks: list[CheckModel]


class UserModel(BaseModel):
    id: int
    username: str
