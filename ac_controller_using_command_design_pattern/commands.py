from command_interface import Command


class PowerOnCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.power_on()

    def undo(self):
        self.ac.power_off()


class PowerOffCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.power_off()

    def undo(self):
        self.ac.power_on()


class TemperatureUpCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.increase_temperature()

    def undo(self):
        self.ac.decrease_temperature()


class TemperatureDownCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.decrease_temperature()

    def undo(self):
        self.ac.increase_temperature()


class SetModeCommand(Command):
    def __init__(self, ac, mode):
        self.ac = ac
        self.mode = mode
        self.old_mode = None

    def execute(self):
        self.old_mode = self.mode
        self.ac.set_mode(self.mode)

    def undo(self):
        self.ac.set_mode(self.old_mode)
    