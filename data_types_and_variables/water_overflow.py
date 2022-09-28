tank_capacity = 255
liters_poured = 0
number_lines = int(input())
for number in range(number_lines):
    current_pour = int(input())
    if tank_capacity - current_pour >= 0:
        tank_capacity -= current_pour
        liters_poured += current_pour
    else:
        print("Insufficient capacity!")
        continue
print(liters_poured)