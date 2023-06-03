# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string = input("Enter your string of words\n")
symbol = input("Enter your symbol\n")
first_letter = string[0]

string = string.replace(first_letter, symbol)
print(string)

