number_of_snowballs = int(input())
max_value = 0
best_weight = 0
best_time = 0
best_quality = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = (snowball_weight // snowball_time) ** snowball_quality
    if current_snowball_value > max_value:
        max_value = current_snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_weight} : {best_time} = {max_value} ({best_quality})")
