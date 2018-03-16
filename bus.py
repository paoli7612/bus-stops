from data import Data
data = Data("lines.xml")

class Bus:
    def __init__(self, id):
        self.id = id
        self.next_stop = 0
        self.lines = data.get_line(self.id)

    def __str__(self):
        text = ("Bus %s\n" % self.id)
        text += ("Next stop: %s\n" %self.lines[self.next_stop])
        return text
