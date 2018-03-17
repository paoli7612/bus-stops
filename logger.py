import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename='log/base.log',level=logging.DEBUG)
        self.info = logging.info
        self.debug = logging.debug
        self.error = logging.error
        self.critical = logging.critical
