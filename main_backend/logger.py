"""
Global log for unique format.

Usage:
from main_backend.logger import logger

log = logger.getChild("path_to_file")

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
