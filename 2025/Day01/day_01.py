class Dial:
    def __init__(self, number) :
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value % 99

    def rotate(self, rotation) :
        direction_char = rotation[:1]
        direction_number = int(rotation[1:])

        if direction_char == 'R':
            self.number += direction_number

        elif direction_char == 'L':
            self.number -= direction_number

        print(self)

    def __str__(self):
        return str("Lock is at: " + str(self.number))


dummyValues = [
    "R13",
    "L5",
    "L3",
    "R5",
    "L2",
    "R2",
    "L1",
    "R1",
    "R120",
    "R423",
    "L70",
    "R4"
]

dial = Dial(50)

for rotation in dummyValues:
    dial.rotate(rotation)