number_companions = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        number_companions -= 2
    if day % 15 == 0:
        number_companions += 5
    coins += 50
    coins -= 2 * number_companions
    if day % 3 == 0:
        coins -= 3 * number_companions
    if day % 5 == 0:
        coins += 20 * number_companions
        if day % 3 == 0:
            coins -= 2 * number_companions
coins_per_companion = coins // number_companions
print(f"{number_companions} companions received {coins_per_companion} coins each.")
