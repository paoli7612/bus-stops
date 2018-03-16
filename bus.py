from threading import Thread
from time import sleep

class Bus:
    def __init__(self, id, program):
        self.id = id
        self.program = program
        self.next_stop = 0
        self.lines = self.program.data.get_line(self.id)
        self.thread = Thread(target=self.run)

    def run(self):
        while self.program.running:
            print(self.program.sleep())
            print(self)
            self.next_stop = (self.next_stop + 1) % len(self.lines)


    def start(self):
        self.thread.start()

    def __str__(self):
        text = ("Bus %s\n" % self.id)
        text += ("Next stop: %s\n" %self.lines[self.next_stop])
        return text
