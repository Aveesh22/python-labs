# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = input("Enter your string of words\n")
letter = input("Enter your letter\n")

print(string.index(letter))