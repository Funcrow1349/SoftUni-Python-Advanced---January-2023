from collections import deque

textiles = deque([int(x) for x in input().split()])
meds = deque([int(x) for x in input().split()])

created_items = {
    "MedKit": 0,
    "Bandage": 0,
    "Patch": 0,
}

while textiles and meds:
    current_textile = textiles.popleft()
    current_med = meds.pop()
    current_sum = current_textile + current_med

    if current_sum == 30:
        created_items["Patch"] += 1
    elif current_sum == 40:
        created_items["Bandage"] += 1
    elif current_sum == 100:
        created_items["MedKit"] += 1
    elif current_sum > 100:
        created_items["MedKit"] += 1
        meds[-1] += current_sum - 100
    else:
        meds.append(current_med + 10)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not meds:
    print("Medicaments are empty.")

created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for key, value in created_items:
    if value > 0:
        print(f"{key} - {value}")

if meds:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(meds))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")





