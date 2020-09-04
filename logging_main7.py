import logging
import logging.config
from othermod import add
from othermod import mult


def get_logger(log_file_name):
    config_file = 'config.txt'
    logging.config.fileConfig(config_file, defaults={'logfilename': log_file_name}, disable_existing_loggers=False)
    logger = logging.getLogger("main")
    return logger

logger = get_logger('scratch.log')
logger.info('Hello, World!')
