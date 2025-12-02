import math


class Dial:
    def __init__(self, number):
        self._number = number
        self.number_history = [number]
        self.passed_zero_counter = 0

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
            self.passed_zero_counter += math.floor((self.number + direction_number) / 100)
            self.number += direction_number

        elif direction_char == 'L':
            if self.number - direction_number <= 0 :
                self.passed_zero_counter += math.floor(math.fabs(self.number - direction_number) / 100) + (self.number != 0)
            self.number -= direction_number


        print(self)

    def __str__(self):
        return str("Lock is at: " + str(self.number) + " 0 Counter: " + str(self.passed_zero_counter))


dummyValues = [
    "L160",
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

dial = Dial(50)

for rotation in rotationValues:
    print("Rotating with: " + rotation)
    dial.rotate(rotation)

print(dial.number_history.count(0))
print(dial.passed_zero_counter)
