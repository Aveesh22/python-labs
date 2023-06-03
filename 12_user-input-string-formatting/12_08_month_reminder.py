# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

# Challenge: Modulate the binary search algorithm to do this with nested if statements
# Can you use a dictionary for this? Or a date/time class in python
num = int(input("Enter a number between 1 and 12\n"))
if num < 1 or num > 12:
    print("Error")

if num > 6:

    if num > 9:

        if num > 11:
            print("December")

        elif num < 11:
            print("October")

        else:
            print("November")

    elif num < 9:

        if num < 8:
            print("July")

        else:
            print("August")

    else:
        print("September")

elif num < 6:

    if num < 3:

        if num < 2:
            print("January")

        elif num == 2:
            print("February")

    elif num > 3:

        if num < 5:
            print("April")

        elif num == 5:
            print("May")

    else:
        print("March")

else:
    print("June")