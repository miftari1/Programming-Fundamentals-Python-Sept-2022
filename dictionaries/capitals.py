country_names = input().split(", ")
capitals = input().split(", ")
my_dictionary = {country: capital for country, capital in zip(country_names, capitals)}
for country, capital in my_dictionary.items():
    print(f'{country} -> {capital}')