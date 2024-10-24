#Day 14 : 6 oct 2024 
# palindrome checker
def is_palindrome(word):
    return word == word[::-1] #indexes
word = input("Enter a word to check if it is palindrome:").lower()
if is_palindrome(word):
    print(f"{word.capitalize()} is a palindrome.")
else:
    print(f"{word.capitalize()} is not palindrome.")

#Simple banking System
