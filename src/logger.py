import logging
from configparser import ConfigParser
from datetime import datetime

parser = ConfigParser()
parser.read('/media/zest/codes1/projects/config/db_config.conf')
log_folder = parser.get('log', 'base_path')

filename = log_folder + \
           '/ingestion_' + \
           datetime.now().strftime("%Y_%d_%m_%H%M%S") + '.log'

suffix = datetime.now().strftime("%Y_%d_%m_%H%M%S")


def getlogger(name=None):
    default = "__app__"
    formatter = logging.Formatter('%(levelname)s : %(asctime)s %(filename)s(%(lineno)d) -- %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    log_map = {"__app__": f"{log_folder}/app_{suffix}.log", "__basic_log__": f"{log_folder}/ingestion_{suffix}.log",
               "__advance_log__": "file2.log"}
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger(default)
    fh = logging.FileHandler(log_map[name])
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return logger
