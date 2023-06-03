# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("Give me your honest opinion on something\n")
counter = 0
new = ""

for char in opinion:
    if char == " ":
        new += " "
        continue

    if counter % 2 == 0:
        new += char

    else:
        new += char.upper()

    counter += 1

print(new)