import psutil
from redis import ConnectionError, Redis

from src.env import env
from src.logger import logger
from src.t import CheckModel
from src.utils.misc import convert_size


def check_memory():
    healthy = True
    memory = psutil.virtual_memory()

    if memory.percent > 80:
        healthy = False

    c = CheckModel(
        name="memory",
        healthy=healthy,
        data={
            "percent": memory.percent,
            "available": convert_size(memory.available),
            "total": convert_size(memory.total),
        },
    )

    return c


def check_redis():
    healthy = True

    try:
        r = Redis.from_url(str(env.REDIS_URL), socket_connect_timeout=1)
        r.ping()
    except ConnectionError as e:
        healthy = False
        logger.error(e)

    c = CheckModel(
        name="redis",
        healthy=healthy,
    )

    return c
