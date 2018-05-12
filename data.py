import os
import xml.etree.ElementTree as element_tree

from table import Table
from line import Line

class Data:
    def __init__(self, city):
        self.path = os.path.dirname(__file__)
        self.path_xml = os.path.join(self.path, "data", city + ".xml")
        self.tree = element_tree.parse(self.path_xml)
        self.root = self.tree.getroot()

        self.table = Table()
        for ss in self.root:
            id = ss.attrib["id"]
            l = Line(id)
            for stop in ss:
                l.add(stop.text)
            self.table.add(l)


def get_table(city):
    d = Data(city)
    return d.table
