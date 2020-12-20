from flask import Flask, Response, stream_with_context
import time
import uuid
import random
import logging
from logger import getlogger
from get_log_file import get_log_file
# log_file_name = get_log_file()
# print(log_file_name)
# logging.getLogger(__name__)
logger = getlogger('__app__')

app = Flask(__name__)

# logger.info(" Starting API")


@app.route("/service_api/<int:rowcount>")
def get_ingestion_request(rowcount):
    def f():
        """Generating mock data"""
        for _ in range(rowcount):
            # time.sleep(.2)
            txid = uuid.uuid4()
            # print(txid)
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield f"('{txid}','{uid}',{amount})\n"

    return Response(stream_with_context(f()))


logger.info(" Starting API")
logger.info("Starting App on localhost:8080")

app.run(host='127.0.0.1', port=5002)
# if __name__ == "__main__":
