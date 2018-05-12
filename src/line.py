from stop import Stop

class Line:
    def __init__(self, id):
        self.id = id
        self.current = 0
        self.stops = list()

    def add(self, name):
        s = Stop(name)
        self.stops.append(s)

    def next_stop(self):
        self.current += 1
        self.current %= len(self.stops)

    def current_stop(self):
        return self.stops[self.current]

    def __iter__(self):
        return self.stops.__iter__()

    def __len__(self):
        return len(self.stops)

    def __getitem__(self, i):
        return self.stops[i]

    def __str__(self):
        t = str()
        for stop in self.stops:
            t += str(stop) + "\n"
        return t
