import psutil

from src.t import CheckModel
from src.utils.misc import convert_size


def check_memory():
    memory = psutil.virtual_memory()

    c = CheckModel(
        name="memory",
        healthy=(memory.percent < 80),
        data={
            "percent": memory.percent,
            "available": convert_size(memory.available),
            "total": convert_size(memory.total),
        },
    )

    return c
