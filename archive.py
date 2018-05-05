import xml.etree.ElementTree as element_tree

class Archive:
    def __init__(self, path_city):
        self.tree = element_tree.parse(path_city)
        self.root = self.tree.getroot()

        self.lines = dict()
        for line in self.root:
            id = line.attrib["id"]
            bus_stops = list()
            for stop in line:
                bus_stops.append(stop.text)
            self.lines[id] = bus_stops

        self.stops = list()
        for id in self.lines:
            for stop in self.lines[id]:
                if not stop in self.stops:
                    self.stops.append(stop)


def get_lines(path_city):
    a = Archive(path_city)
    return a.lines
