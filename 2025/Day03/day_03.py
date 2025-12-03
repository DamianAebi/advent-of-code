with open("input.txt", "r") as input_file:
    joltage_lines = [line.strip() for line in input_file.readlines()]

print(joltage_lines)

# 1. -> search the highest digit in the line (if there are multiple, then the left-most)
# 2. -> if there are any to the right of it, take the highest from the right
# 3. -> if there are none to the right of it, take the highest from the left

joltage_numbers = []


def pick_highest_int_from_list(num_list) -> str:
    return str(max(num_list))

swap = False

def pick_second_highest_int_from_list(num_list, highest) -> str:
    highest_index = num_list.index(highest)
    if highest_index == len(num_list) - 1:  # if the hightest digit is all the way at the end
        global swap
        swap = True
        return pick_highest_int_from_list(num_list[:-1])
    else:
        return pick_highest_int_from_list(num_list[highest_index + 1:])


dummy_values = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111'
]

for line in joltage_lines:
    left_digit = pick_highest_int_from_list([int(char) for char in line])
    right_digit = pick_second_highest_int_from_list([int(char) for char in line], int(left_digit))

    if not swap:
        print("appending: " + left_digit + right_digit)
        joltage_numbers.append(left_digit + right_digit)
    else:
        print("appending: " + right_digit + left_digit)
        joltage_numbers.append(right_digit + left_digit)

    swap = False

print(sum([int(joltage_number) for joltage_number in joltage_numbers]))
