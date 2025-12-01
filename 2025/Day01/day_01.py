class Dial:
    def __init__(self, number):
        self._number = number
        self.number_history = [number]

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value % 100
        self.number_history.append(self._number)

    def rotate(self, rotation):
        direction_char = rotation[:1]
        direction_number = int(rotation[1:])

        if direction_char == 'R':
            self.number += direction_number

        elif direction_char == 'L':
            self.number -= direction_number

        # print(self)

    def __str__(self):
        return str("Lock is at: " + str(self.number))


dummyValues = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
]

with open("input.txt", "r") as input_file:
    rotationValues = [line.strip() for line in input_file]
    print(rotationValues)

dial = Dial(50)

for rotation in rotationValues:
    dial.rotate(rotation)

print(dial.number_history)
print(dial.number_history.count(0))
