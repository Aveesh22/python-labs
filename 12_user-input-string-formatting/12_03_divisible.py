# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

num = int(input("Enter your number\n"))

if num % 3 == 0:
    print("Number is divisible by 3")

else:
    print("Number is not divisible by 3")