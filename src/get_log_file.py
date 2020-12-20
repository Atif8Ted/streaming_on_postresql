from configparser import ConfigParser
from datetime import datetime
parser = ConfigParser()
parser.read('/media/zest/codes1/projects/config/db_config.conf')
log_folder = parser.get('log', 'base_path')

filename = log_folder + \
           '/ingestion_' + \
           datetime.now().strftime("%Y_%d_%m_%H%M%S") + '.log'

def get_log_file():

    return filename
