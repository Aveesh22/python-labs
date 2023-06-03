# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = int(input("Enter your investment amount\n"))
interest_rate = float(input("Enter your interest rate as a percentage\n"))
years = int(input("Enter the number of years you will invest\n"))

print(investment * ((1 + interest_rate * .01) ** years))