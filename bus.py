
class Bus:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.next_stop = 0
        self.lines = self.data.get_line(self.id)

    def __str__(self):
        text = ("Bus %s\n" % self.id)
        text += ("Next stop: %s\n" %self.lines[self.next_stop])
        return text
