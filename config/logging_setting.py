import logging
from logging.config import fileConfig
import os
class LogConfig():

    @staticmethod
    def get_logger():
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"logging.ini")
        logging.config.fileConfig(file_path)
        logger = logging.getLogger(name="DaineTest")
        return logger

if __name__ == '__main__':

    logger = LogConfig.get_logger()
    logger.info("测试")


