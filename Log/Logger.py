import logging
from logging.handlers import RotatingFileHandler


class LoggerInstance:

    @staticmethod
    def get_logger(name, path):
        logger = logging.getLogger(name)
        msg_format = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(msg_format)
        # datefmt = '%m/%d/%Y %I:%M:%S %p'
        file_handler = RotatingFileHandler(path, mode='a', maxBytes=1024**2, backupCount=5)
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(level)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        return logger
