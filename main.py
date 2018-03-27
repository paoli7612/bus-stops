from bus import Bus
from archive import Data
from time import sleep
from random import randint
from logger import Logger
from gui.window import Gui
from arg import Argparser

class Program:
    def __init__(self):
        self.parser = Argparser()
        self.city = self.parser.city
        self.data = Data(self.city)
        self.running = True
        self.logger = Logger("log/base.log")
        self.logger.start()
        self.window = Gui(self)
        self.all_bus = dict()
        for k in self.data.lines:
            self.all_bus[k] = Bus(k,self)
            self.all_bus[k].start()
            self.sleep()
        raw_input("Premi INVIO per terminare il programma")
        self.running = False
        self.logger.quit()

    def sleep(self):
        delay = float(randint(2,12))/10.0
        sleep(delay)
        return delay

if __name__ == "__main__":
    Program()
