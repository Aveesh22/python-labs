# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


one = input("Enter your first string\n")
two = input("Enter your second string\n")
three = input("Enter your third string\n")
longest = ""

if len(one) > len(two) and len(one) > len(three):
    longest = one

elif len(two) > len(one) and len(two) > len(three):
    longest = two

else:
    longest = three

print(f"{len(longest)}, {longest}")