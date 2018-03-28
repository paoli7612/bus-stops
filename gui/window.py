import turtle

class Gui:
    def __init__(self, program):
        turtle.setup(1200,600)
        self.program = program
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.show_lines()

    def write(self,text,pos):
        self.pen.goto(pos)
        self.pen.write(text)

    def show_lines(self):
        posx = -turtle.window_width()/2
        for id, bus_stops in self.program.ram.lines.items():
            posy = 200
            self.pen.goto(posx,210)
            self.pen.write("LINEA: %s" %id)
            for bus_stop in bus_stops:
                self.pen.goto(posx,posy)
                self.pen.write(" - %s" %str(bus_stop))
                posy-=10
            posx += 200
