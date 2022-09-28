character_to_start = int(input())
character_to_end = int(input())
for symbol in range(character_to_start, character_to_end + 1):
    print(chr(symbol), end=" ")
