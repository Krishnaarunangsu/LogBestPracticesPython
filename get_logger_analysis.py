import logging
import pandas as pd


def get_logger(present_file, mode='DEBUG'):
    """ insert comments """
    my_logger = logging.getLogger(present_file)

    # MASTER_FOLDER = '../DataFolder/'
    # LOG_FOLDER =  MASTER_FOLDER + 'LogFolder/'
    # LOG_CREATOR = LOG_FOLDER + 'log_creator.csv'
    # Need to understand the following two lines from the functional perspective
    log_creator_data = pd.read_csv(constants.LOG_CREATOR)
    log_file_name = str(list(log_creator_data[log_creator_data['module_name'] == present_file]['filename'])[0])

    # The following three lines should be handled in properties file not in .py file
    # according to industry standards
    handler = logging.FileHandler(log_file_name)
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)

    # This checking  and setting should not be manual
    if mode == 'INFO':
        my_logger.setLevel(logging.INFO)
    else:
        my_logger.setLevel(logging.DEBUG)
    return my_logger
