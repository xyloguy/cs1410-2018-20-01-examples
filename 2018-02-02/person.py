class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def get_name(self):
        return self.name

    def get_ssn(self):
        return self.ssn

    def __str__(self):
        return 'Name: ' + self.get_name() + ', SSN: ' + self.get_ssn()
