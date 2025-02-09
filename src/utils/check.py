import psutil

from src.t import CheckModel


def check_memory():
    memory = psutil.virtual_memory()

    c = CheckModel(
        name="memory",
        healthy=(memory.percent < 80),
        data={
            "percent": memory.percent,
            "available": memory.available,
            "total": memory.total,
        },
    )

    return c
