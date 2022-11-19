from math import ceil
budget = float(input())
number_students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
number_flour_packets = number_students - number_students // 5
total_aprons = ceil(number_students + number_students * 0.2)
cost_flour = number_flour_packets * flour_price
cost_eggs = number_students * (egg_price * 10)
cost_aprons = total_aprons * apron_price
total_cost = cost_flour + cost_eggs + cost_aprons
if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed. ")