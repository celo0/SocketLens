import logging
import datetime

def setup_logger():
    data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler(f'socketlens_{data}.log'), logging.StreamHandler()]
    )

def get_logger():
    return logging.getLogger()