class Student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = float(age)

    def __str__(self):
        return self.ssn + ": " + self.last + ' ' + self.first
