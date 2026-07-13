from receiver_ac import AirConditioner
from invoker_remote import Remote
from commands import PowerOnCommand, PowerOffCommand, TemperatureUpCommand, TemperatureDownCommand, SetModeCommand


if __name__ == "__main__":
    ac = AirConditioner()
    remote = Remote()

    remote.press_button(PowerOnCommand(ac))
    remote.press_button(SetModeCommand(ac, "FAN"))
    remote.press_button(TemperatureUpCommand(ac))
    remote.press_button(TemperatureDownCommand(ac))
    remote.undo()
    remote.redo()
    remote.press_button(PowerOffCommand(ac))

    
