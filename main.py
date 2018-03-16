from bus import Bus
from archive import Data
class Program:
    def __init__(self, city):
        self.city = city
        self.data = Data(self.city)
        print(self.data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1: print("Immettere il nome della citta'")
    elif len(sys.argv) > 2: print("Immettere solo una citta")
    else: program = Program(sys.argv[1])
