class StopList:
    def __init__(self):
        self.stops = dict()

    def add_line(self, line):
        for stop in line:
            self.add_stop(stop)

    def add_stop(self, stop):
        name = stop.name
        if not name in self.stops:
            self.stops[name] = stop

    def __iter__(self):
        return self.stops.values().__iter__()

    def __getitem__(self, key):
        return self.stops[key]
