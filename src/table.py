from stop_list import StopList

class Table:
    def __init__(self):
        self.lines = dict()
        self.stop_list = StopList()

    def add(self, line):
        id = line.id
        self.lines[id] = line
        self.stop_list.add_line(line)

    def __getitem__(self, key):
        return(self.lines[key])

    def __str__(self):
        t = str()
        for id,line in self.lines.items():
            t += str(id) + "\n" + str(line) + "\n"
        return t
