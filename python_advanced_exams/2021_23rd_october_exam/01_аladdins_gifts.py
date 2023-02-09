from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

presents_dict = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            result = current_material * 2 + current_magic * 3
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        presents_dict["Gemstone"] += 1
    elif 200 <= result <= 299:
        presents_dict["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        presents_dict["Gold"] += 1
    elif 400 <= result <= 499:
        presents_dict["Diamond Jewellery"] += 1

if (presents_dict["Gemstone"] and presents_dict["Porcelain Sculpture"]) or \
        (presents_dict["Gold"] and presents_dict["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, amount in sorted(presents_dict.items()):
    if amount > 0:
        print(f"{present}: {amount}")