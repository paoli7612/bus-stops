from threading import Thread
from time import sleep
from colors import Colors

class Bus:
    def __init__(self, id, program):
        self.id = id
        self.program = program
        self.next_stop = 0
        self.stops = self.program.data.get_line(self.id)
        self.thread = Thread(target=self.run)
        self.program.logger.debug("Create new bus: " + self.id)

    def run(self):
        while self.program.running:
            self.program.logger.info(self)
            self.next_stop = (self.next_stop + 1) % len(self.stops)
            self.program.logger.info(self.program.sleep())


    def start(self):
        self.thread.start()

    def __str__(self):
        text = ("Bus %s\n" % self.id)
        text += ("Next stop: %s\n" %self.stops[self.next_stop])
        return text
