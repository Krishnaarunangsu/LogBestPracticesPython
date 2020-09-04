import os
import logging
import logging.config

from configparser import ConfigParser

parser = ConfigParser()
parser.read('resources/log_details_location.conf')

# print(parser.get('database_config', 'url'))
log_properties_file = parser.get('log_details_config', 'log_properties_file')
print(log_properties_file)
log_output_file = parser.get('log_details_config', 'log_output_file')
print(log_output_file)
# if os.environ['COMPUTERNAME'] == 'WIN-E39OLKT8K4F':
# print(parser.get('UK_PDL', 'db.user_name'))


def get_logger(log_properties_file, log_file_name):
    config_file = 'D:/Arunangsu/resources/logging4.conf'
    # logging.config.fileConfig(config_file, defaults={'logfilename': 'D://Arunangsu//Logs//testSuite_new.log'}, disable_existing_loggers=False)
    logging.config.fileConfig(config_file, defaults={'logfilename': log_file_name}, disable_existing_loggers=False)
    logger = logging.getLogger("main")
    return logger

logger = get_logger(log_properties_file, log_output_file)
logger.debug('Hi')
