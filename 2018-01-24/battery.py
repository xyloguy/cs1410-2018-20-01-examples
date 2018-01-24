MAX_CHARGE = 20000

class Battery:
    def __init__(self):
        self.remaining_milliamps = MAX_CHARGE
        self.voltage = 5
        self.amps = 3.1

    def charge(self, milliamps):
        if milliamps <= 0:
            return 0

        self.remaining_milliamps += milliamps
        if self.remaining_milliamps > MAX_CHARGE:
            self.remaining_milliamps = MAX_CHARGE

    def drain(self, milliamps):
        if milliamps <= 0:
            return 0

        for i in range(milliamps):
            if self.remaining_milliamps == 0:
                return i
            self.remaining_milliamps -= 1
        return milliamps

b = Battery()
print(b.drain(20050))
