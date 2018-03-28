from archive import Data

class Ram:
    def __init__(self, city):
        self.data = Data(city)

        self.city = self.data.city
        self.lines = self.data.lines
        self.stops = self.data.stops

    def show(self):
        print(self.city)
        for line in self.lines:
            print(line)

        for stop in self.stops:
            print(stop)
