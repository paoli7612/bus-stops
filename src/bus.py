from copy import copy

class Bus:
    def __init__(self, id, line):
        self.id = id
        self.line = copy(line)

    def current_stop(self):
        return self.line.current_stop()

    def next_stop(self):
        self.line.next_stop()
        return self.current_stop()

    def __str__(self):
        return str(self.id)
