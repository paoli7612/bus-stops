from colors import Colors
class Info:
    def __init__(self, args):
        self.len_args = len(args)
        if self.len_args == 1 or args[1] == "help":
            self.show_help()
        elif args[1] == "lines" and self.len_args == 3:
            self.state = "lines"
            self.city = args[2]
            self.show_lines()
        elif args[1] == "cities":
            self.state = "cities"
            self.show_cities()
        else: self.show_help()



    def show_help(self):
        print(Colors.RED + "HELP" + Colors.WHITE)
        print("use: python info.py lines [city]")
        print("  to see all lines of [city]\n")

        print("use: python info.py cities")
        print("  to see all cities\n")

    def show_lines(self):
        print(Colors.BLUE + "LINES" + Colors.WHITE + " of " + Colors.TAN + self.city)
        from archive import Data
        data = Data(self.city)
        print(Colors.WHITE)
        print(data)

    def show_cities(self):
        print(Colors.ORANGE + "CITIES")

if __name__ == "__main__":
    import sys
    Info(sys.argv)
