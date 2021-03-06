"""
Global log for unique format.

Usage:
from core.logger import logger

log = logger.getChild("__name__")

log.debug('message')
log.info('message')
log.warning('message')
log.error('message')
log.critical('message')
"""
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger()

stream_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
