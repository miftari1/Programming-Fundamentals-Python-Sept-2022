text_list = input().split(", ")
int_values_list = []
#conversing the str values from the text_list into int values and adding them to the new int_values_list
for amount in text_list:
    amount = int(amount)
    int_values_list.append(amount)

count_of_beggars = int(input())
collected_sum = 0
beggars_savings_list = []
for beggar in range(count_of_beggars):
    collected_sum = sum(int_values_list[beggar::count_of_beggars])
    beggars_savings_list.append(collected_sum)
print(beggars_savings_list)
