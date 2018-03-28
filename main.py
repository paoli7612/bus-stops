from bus import Bus
from logger import Logger
from gui.window import Gui
from arg import Argparser
from ram import Ram

from random import randint
from time import sleep

class Program:
    def __init__(self):
        self.parser = Argparser()
        self.ram = Ram(self.parser.city)
        self.logger = Logger("log/base.log")
        self.window = Gui(self)
        self.running = True
        self.logger.start()
        self.run()

    def run(self):
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
