class Podracer:
    def __init__(self):
        self.mSpeed = 0
        self.mHeat = 0

    def setSpeed(self, speed):
        self.mSpeed = speed
        self.mHeat = speed * 1.5

    def turboSpeed(self):
        self.mSpeed *= 2
        self.mHeat *= 4

    def checkEngines(self):
        if self.mHeat < 24:
            return "Nominal"
        elif self.mHeat < 48:
            return "Warning!"
        return "MALFUNCTION!!"

ani = Podracer() # 0, 0
ani.setSpeed(2) # 2, 3
ani.turboSpeed() # 4, 12
ani.turboSpeed() # 8, 48
print(ani.checkEngines()) # MALFUNCTION!!

sebulba = Podracer() # 0, 0
sebulba.setSpeed(6) # 6, 9
sebulba.turboSpeed() # 12, 36
print(sebulba.checkEngines()) # Warning!