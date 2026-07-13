class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 24
        self.mode = "COOL"

    def power_on(self):
        self.is_on = True
        print("Power ON")

    def power_off(self):
        self.is_on = False
        print("Power OFF")

    def increase_temperature(self):
        self.temperature += 1
        print(f"Temperature: {self.temperature}")

    def decrease_temperature(self):
        self.temperature -= 1
        print(f"Temperature: {self.temperature}")

    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode: {self.mode}")

