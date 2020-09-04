import logging, logging.config

# set up logging
logging.config.fileConfig("resources/scratch.ini")
# logger = logging.getLogger('sLogger')
logger = logging.getLogger(__name__)
# log something
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
