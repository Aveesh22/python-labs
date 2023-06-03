# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

n = len(filename)
i = n-4
counter = 0
boolean = True

while(i < n):
    if counter == 0 and not filename[i] == ".":
        boolean = False
        break
    elif counter == 1 and not filename[i] == "p":
        boolean = False
        break
    elif counter == 2 and not filename[i] == "d":
        boolean = False
        break
    elif counter == 3 and not filename[i] == "f":
        boolean = False
        break
    i += 1
    counter += 1

if boolean == False:
    print("Not a .pdf file")

else:
    print("This is a .pdf file")




