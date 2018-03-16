import xml.etree.ElementTree as element_tree

class Data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tree = element_tree.parse(self.file_name)
        self.root = self.tree.getroot()
        self.lines = dict()
        for element_line in self.root:
            id = element_line.attrib["id"]
            bus_stops = list()
            for element_busStop in element_line:
                bus_stops.append(element_busStop.text)
            self.lines[id] = bus_stops

    def get_line(self, id):
        if not id in self.lines:
            print("Servizio non disponibile")
        else: return self.lines[id]
