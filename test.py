import cmd

from simulation import Simulation

class Cli(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "-> "
        self.sim = Simulation()

    def run(self): self.cmdloop()
    def do_quit(self, arg): return True
    def do_show(self, arg): print(self.sim)
    def do_stop(self, arg): self.sim.stop()
    def do_bus(self, arg):
        if not arg: print(self.sim.station)
        else:
            try: self.sim.new_bus(arg)
            except: pass
    def do_line(self, arg):
        self.sim.show_line(arg)

c = Cli()
c.do_bus("1")
c.do_line("1")
c.run()
