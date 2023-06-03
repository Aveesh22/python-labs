# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_input = input("Enter your string to find the number of vowels\n")
a = 0
e = 0
i = 0
o = 0
u = 0

for char in user_input:
    if char == "a":
        a += 1
    if char == "e":
        e += 1
    if char == "i":
        i += 1
    if char == "o":
        o += 1
    if char == "u":
        u += 1

print(f"The number of times a appeared was {a} times \nThe number of times e appeared was {e} times \nThe number of times i appeared was {i} times    \nThe number of times o appeared was {o} times  \nThe number of times u appeared was {u} times")



