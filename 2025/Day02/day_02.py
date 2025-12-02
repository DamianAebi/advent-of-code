with open("input.txt", "r") as input_file:
    id_ranges = input_file.readline().strip().split(",")

print(id_ranges)

id_sum = 0

def is_repeating_pattern(n: int) -> bool:
    s = str(abs(n))  # handle negatives if needed
    if len(s) < 2:
        return False

    # Check every possible pattern length up to half the string
    for k in range(1, len(s) // 2 + 1):
        if len(s) % k == 0:
            pattern = s[:k]
            if pattern * (len(s) // k) == s:
                print(pattern + " found in string: " + s)
                return True
    return False


def is_valid_id(id: int) -> bool:
    return not (is_repeating_pattern(id) or str(id).startswith("0"))


for id_range in id_ranges:
    range_min, range_max = id_range.split("-")
    for i in range(int(range_min), int(range_max) + 1):
        if not is_valid_id(i):
            id_sum += i

print(id_sum)