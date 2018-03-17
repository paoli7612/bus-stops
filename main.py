from bus import Bus
from archive import Data
from time import sleep
from random import randint
from logger import Logger

class Program:
    def __init__(self, city):
        self.city = city
        self.data = Data(self.city)
        self.running = True
        self.logger = Logger("log/base.log")
        self.logger.start()
        b = Bus("1",self)
        raw_input("Premi INVIO per terminare il programma")
        self.running = False
        self.logger.quit()

    def sleep(self):
        delay = float(randint(2,12))/10.0
        sleep(delay)
        return delay

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1: print("Immettere il nome della citta'")
    elif len(sys.argv) > 2: print("Immettere solo una citta")
    else: program = Program(sys.argv[1])
