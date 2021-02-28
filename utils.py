"""
    Utilities
"""
import re
import time
from datetime import datetime
import logging

import constant

def get_filename(prefix, extension, is_everyday=None):
    """
        Return filename everyday with prefix

        @Example: get_filename_everyday('test', 'csv', true)
        will return: 'test_2021_02_21.csv'
    """
    if is_everyday is False:  # Every second
        return prefix + '_' + re.sub('[ :]', '_', str(time.asctime())) + '.' + extension
    elif is_everyday is True:
        return prefix + '_' + re.sub('-', '_', str(datetime.now())[0:10]) + '.' + extension
    else:
        return prefix + '.' + extension


def log(process_name, is_end_log=None, message=None):
    """
        Logger
    """
    logging.basicConfig(format=constant.FORMAT_LOG, datefmt=constant.FORMAT_DATE,
                        filename=constant.FILE_NAME, level=logging.INFO)
    if is_end_log is not None:
        msg = '[INFO ] ' + 'Finish ' + process_name + " " + message
        logging.info(msg)
        print(msg)
    else:
        msg = '[INFO ] ' + 'Start ' + process_name
        logging.info(msg)
        print(msg)


def error_log(process_name, message):
    """ Error log"""
    logging.basicConfig(format=constant.FORMAT_LOG, datefmt=constant.FORMAT_DATE,
                        filename=constant.FILE_NAME, level=logging.ERROR)
    msg = "[ERROR] " + process_name + " went wrong because of: "+ "\n" + message
    logging.error(msg)
    print(msg)
