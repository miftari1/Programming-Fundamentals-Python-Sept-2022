key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
is_obtained = False
while not is_obtained:
    materials = input().split(" ")
    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        material = materials[index + 1].lower()
        if material not in key_materials:
            key_materials[material] = 0
        key_materials[material] += quantity
        if key_materials[material] >= 250:
            if material == 'shards' or material == 'fragments' or material == 'motes':
                print(f'{legendary_items[material]} obtained!')
                key_materials[material] -= 250
                is_obtained = True
                break
    if is_obtained:
        break
for material, quantity in key_materials.items():
    print(f'{material}: {quantity}')