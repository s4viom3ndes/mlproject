import logging 
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == "__main__":

    try:
        logging.info("Logging has started.")
        a = 1/0
    except Exception as e:
        logging.exception(e)
    #logging.info("Logging has started.")