#   This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
#   First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
#   After that, you will be given another sequence of integers – their magic level.
#   Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic
#   level:
#
#   Present	      Magic needed
#   Doll	      150
#   Wooden train  250
#   Teddy bear	  300
#   Bicycle 	  400
#
#   You should take the last box with materials and the first magic level value to craft a toy. Their multiplication
#   calculates the total magic level. If the result equals one of the levels described in the table above, you craft
#   the present and remove both materials and magic value. Otherwise:
#   •	If the product of the operation is a negative number, you should sum the values together, remove them both from
#       their positions, and add the result to the materials.
#   •	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the
#       magic value and increase the material value by 15.
#   •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
#   Stop crafting presents when you run out of boxes of materials or magic level values.
#   Your task is considered done if you manage to craft either one of the pairs:
#   •	a doll and a train
#   •	a teddy bear and a bicycle
#   Input
#   •	The first line of input will represent the values of boxes with materials - integers, separated by a single space
#   •	On the second line, you will be given the magic values - integers again, separated by a single space
#   Output
#   •	On the first line - print whether you've succeeded in crafting the presents:
#       o	"The presents are crafted! Merry Christmas!"
#       o	"No presents this Christmas!"
#   •	On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
#       o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
#       o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
#   •	On the next lines print the presents you have crafted, ordered alphabetically in the format:
#       o	"{toy_name1}: {amount}
#            {toy_name2}: {amount}
#            ...
#            {toy_nameN}: {amount}"
#   Constraints
#   •	All the materials' values will be integers in the range [1, 100]
#   •	Magic level values will be integers in the range [-10, 100]
#   •	In all cases, at least one present will be crafted

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

crafted_toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
task_successful = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    if current_material == 0 or current_magic == 0:
        if current_material == 0 and current_magic != 0:
            magic.appendleft(current_magic)
            continue
        elif current_material != 0 and current_magic == 0:
            materials.append(current_material)
            continue
        else:
            continue

    product = current_material * current_magic
    if product == 150:
        crafted_toys["Doll"] += 1
    elif product == 250:
        crafted_toys["Wooden train"] += 1
    elif product == 300:
        crafted_toys["Teddy bear"] += 1
    elif product == 400:
        crafted_toys["Bicycle"] += 1
    elif product < 0:
        materials.append(current_material + current_magic)
    else:
        materials.append(current_material + 15)

if (crafted_toys["Doll"] > 0 and crafted_toys["Wooden train"] > 0) or (crafted_toys["Teddy bear"] > 0 and crafted_toys["Bicycle"] > 0):
    task_successful = True

if task_successful:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key in sorted(crafted_toys.keys()):
    if crafted_toys[key] > 0:
        print(f"{key}: {crafted_toys[key]}")