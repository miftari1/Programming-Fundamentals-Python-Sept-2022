numbers_sequence = input().split(", ")
positive = [int(number) for number in numbers_sequence if int(number) >= 0]
negative = [int(number) for number in numbers_sequence if int(number) < 0]
even = [int(number) for number in numbers_sequence if int(number) % 2 == 0]
odd = [int(number) for number in numbers_sequence if int(number) != 0 and int(number) % 2 != 0]
print(f"Positive: {', '.join([str(number) for number in positive])}")
print(f"Negative: {', '.join([str(number) for number in negative])}")
print(f"Even: {', '.join([str(number) for number in even])}")
print(f"Odd: {', '.join([str(number) for number in odd])}")