words_sequence_list = input().split()
palindrome = input()
list_palindromes = [current_word for current_word in words_sequence_list if current_word == current_word[::-1]]
count_given_palindrome = list_palindromes.count(palindrome)
print(list_palindromes)
print(f"Found palindrome {count_given_palindrome} times")