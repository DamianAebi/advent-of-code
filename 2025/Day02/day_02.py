with open("input.txt", "r") as input_file:
    id_ranges = input_file.readline().strip().split(",")

print(id_ranges)

id_sum = 0


def is_repeating_pattern(n: int) -> bool:
    s = str(abs(n))
    if len(s) < 2 or len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]



def is_valid_id(id: int) -> bool:
    return not (str(id).startswith("0") or is_repeating_pattern(id))


dummy_values = [
    '11-22',
    '95-115',
    '998-1012',
    '1188511880-1188511890',
    '222220-222224',
    '1698522-1698528',
    '446443-446449',
    '38593856-38593862',
]

for id_range in id_ranges:
    range_min, range_max = id_range.split("-")
    for i in range(int(range_min), int(range_max) + 1):
        if not is_valid_id(i):
            id_sum += i

print(id_sum)
