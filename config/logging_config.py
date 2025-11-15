import logging
from logging.handlers import RotatingFileHandler


""" Setup the logger """
def setup_logging():

    # create root logger
    logger = logging.getLogger("app_log")
    logger.setLevel(logging.INFO)

    #format for the logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # for console display
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # for file display
    file_handler = RotatingFileHandler('app.log', maxBytes=1_000_000, backupCount=3)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
