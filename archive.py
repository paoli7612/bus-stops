import xml.etree.ElementTree as element_tree
import os
class Data:
    def __init__(self, city):
        self.all_cities = os.listdir(os.getcwd()+"/data/")
        self.city = city
        if not self.city + ".xml" in self.all_cities:
            print("Citta' non presente nel archivio")
            exit(0)

        self.file_name = "data/" + self.city + ".xml"

        self.tree = element_tree.parse(self.file_name)
        self.root = self.tree.getroot()
        self.lines = self.get_lines()
        self.stops = self.get_stops()

    def get_lines(self):
        lines = dict()
        for element_line in self.root:
            id = element_line.attrib["id"]
            bus_stops = list()
            for element_busStop in element_line:
                bus_stops.append(element_busStop.text)
            lines[id] = bus_stops
        return lines

    def get_stops(self):
        stops = list()
        for id in self.lines:
            for stop in self.lines[id]:
                if not stop in stops:
                    stops.append(stop)
        return stops


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
