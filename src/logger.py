import sys

from loguru import logger


logger.remove(0)
logger.add(sys.stdout, level="INFO")
logger.add(sys.stdout, level="SUCCESS")
logger.add(sys.stderr, level="WARNING")
logger.add(sys.stderr, level="ERROR")
logger.add(sys.stderr, level="CRITICAL")
