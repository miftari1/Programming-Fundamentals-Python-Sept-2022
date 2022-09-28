year = int(input())
is_found = False
while not is_found:
    year += 1
    c = set()
    for digit in str(year):
        c.add(digit)
    if len(c) == len(str(year)):
        is_found = True
print(year)