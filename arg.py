import argparse

description = "Select a city to see"

class Argparser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument("city", metavar="CITY", type=str, help="Select city")
        self.args = self.parser.parse_args()
        self.city = self.args.city
