import xml.etree.ElementTree as element_tree

class Data:
    def __init__(self, file_name):
        self.file_name = "data/" + file_name + ".xml"
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

    def __str__(self):
        text = str()
        for id, bus_stops in self.lines.items():
            text += ("LINEA: %s\n" %id)
            for bus_stop in bus_stops:
                text += (" - %s\n" %str(bus_stop))
            text += "\n"
        return text
