from typing import Any, Optional

from pydantic import (BaseModel, PositiveInt, RedisDsn, SecretStr, StrictBool,
                      StrictStr)


class EnvModel(BaseModel):
    DEBUG: bool
    PORT: PositiveInt
    SECRET_KEY: SecretStr
    JWT_ACCESS_TOKEN_EXPIRES: PositiveInt
    DATA_FILE_PATH: StrictStr
    REDIS_URL: RedisDsn
    # DATABASE_URL: PostgresDsn


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
