number_of_lines = int(input())
symbol_sequence = ""
result = ""
for num in range(number_of_lines):
    user_input = input()
    if user_input == "(" or user_input == ")":
        symbol_sequence += user_input
if symbol_sequence[0] == ")":
    result = "UNBALANCED"
elif "((" in symbol_sequence:
    result = "UNBALANCED"
else:
    result = "BALANCED"
print(result)