import configparser
import psycopg2
import requests
import logging
from logger import getlogger
from get_log_file import get_log_file
# log_file_name = get_log_file()
# logging.getLogger(__name__)
logger = getlogger('__basic_log__')
parser = configparser.ConfigParser()
parser.read('/media/zest/codes1/projects/config/db_config.conf')
host = parser.get('postgres_config', 'host')
user = parser.get('postgres_config', 'user')
database = parser.get('postgres_config', 'database')
password = parser.get('postgres_config', 'password')
port = parser.get('postgres_config', 'port')

logger.info("Starting to Write to Postgresql DB")
with requests.get("http://localhost:5002/service_api/10", stream=True)as r:
    conn = psycopg2.connect(host=host,
                            port=port,
                            user=user,
                            database=database,
                            password=password
                            )
    print(conn)
    print("Connection Succeeded")
    cursor = conn.cursor()
    sql = """INSERT INTO zest.transactions (txid,uid,amount)
            values ('{0}','{1}','{2}')"""
    buffer = ""
    try:
        for chunk in r.iter_content(chunk_size=1):
            if chunk.endswith(b'\n'):
                t = eval(buffer)
                print(t)
                insert_sql = sql.format(t[0], t[1], t[2])
                logger.info(insert_sql)
                cursor.execute(insert_sql)
                conn.commit()
                buffer = ""
            else:
                buffer = buffer + chunk.decode()
    except BaseException as e:
        pass
        logger.error("Process Aborted : " + str(e))

logger.info("Finished")
