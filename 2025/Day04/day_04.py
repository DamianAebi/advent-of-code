def split_file_on_blank_line(path: str):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    try:
        i = lines.index("")          # first blank line
    except ValueError:
        return lines, []             # no blank line found

    _range_strings = lines[:i]
    _ingredient_ids = lines[i+1:]
    return _range_strings, _ingredient_ids

range_strings, ingredient_ids = split_file_on_blank_line('input.txt')

print(range_strings)
print(ingredient_ids)

ranges = []

for range_string in range_strings:
    split = range_string.split('-')
    min_id = int(split[0])
    max_id = int(split[-1])
    ranges.append(range(min_id, max_id + 1))

fresh_count = 0

def is_ingredient_fresh(ingredient_id):
    for range in ranges:
        if int(ingredient_id) in range:
            return True

    return False

for ingredient_id in ingredient_ids:
    if is_ingredient_fresh(ingredient_id):
        fresh_count += 1


print(fresh_count)