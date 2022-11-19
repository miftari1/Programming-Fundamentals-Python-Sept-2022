list_of_fires = input().split("#")
water_amount = int(input())
put_out_cells = []
total_effort = 0
for fire in list_of_fires:
    fire_elements = fire.split(" = ")
    type_of_fire = fire_elements[0]
    cell_value = int(fire_elements[1])
    if type_of_fire == "High" and cell_value in range(81, 125 + 1):
        if water_amount - cell_value >= 0:
            water_amount -= cell_value
            total_effort += 0.25 * cell_value
            put_out_cells.append(cell_value)
        else:
            continue
    elif type_of_fire == "Medium" and cell_value in range(51, 80 + 1):
        if water_amount - cell_value >= 0:
            water_amount -= cell_value
            total_effort += 0.25 * cell_value
            put_out_cells.append(cell_value)
        else:
            continue
    elif type_of_fire == "Low" and cell_value in range(1, 50 + 1):
        if water_amount - cell_value >= 0:
            water_amount -= cell_value
            total_effort += 0.25 * cell_value
            put_out_cells.append(cell_value)
        else:
            continue
print("Cells:")
for value in put_out_cells:
    print(f" - {value}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")