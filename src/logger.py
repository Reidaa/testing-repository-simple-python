import sys

from loguru import logger

from src.env import env

logger.remove(0)
logger.add(sys.stdout, serialize=(not env.DEBUG))
