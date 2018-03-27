import logging
import os

class Logger:
    def __init__(self, file_name, verbose=True):
        logging.basicConfig(filename=file_name,level=logging.DEBUG)
        self.info = logging.info
        self.debug = logging.debug
        self.error = logging.error
        self.critical = logging.critical
        self.verbose = verbose

    def start(self):
        self.info("Start program")

    def quit(self):
        self.info("Endo program\n")
        self.save_log()

    def save_log(self):
        os.chdir("log/")
        file_name = self.get_name_log()
        os.rename("base.log", file_name)

    def get_name_log(self):
        from time import localtime
        data_struct = localtime()
        year = data_struct.tm_year
        month = data_struct.tm_mon
        day = data_struct.tm_mday
        hour = data_struct.tm_hour
        mins = data_struct.tm_min
        data = str(year) + "." + str(month) + "." + str(day)
        moment = str(hour) + "." + str(mins)
        file_name = data + ":" + moment + ".log"
        return file_name
