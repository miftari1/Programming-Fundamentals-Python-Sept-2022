deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    shuffled_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    first_half = deck_of_cards[0:middle_of_deck]
    second_half = deck_of_cards[middle_of_deck::]
    for card_index in range(len(first_half)):
        shuffled_deck.append(first_half[card_index])
        shuffled_deck.append(second_half[card_index])
    deck_of_cards = shuffled_deck
print(deck_of_cards)
