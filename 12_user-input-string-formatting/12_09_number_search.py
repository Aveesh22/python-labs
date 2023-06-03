# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

num = int(input("Enter a number between 0 and 1,000,000\n"))

while int(input("Enter your guess\n")) != num:
    continue
