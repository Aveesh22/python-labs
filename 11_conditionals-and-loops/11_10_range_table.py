# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

for i in range(50):
    if (i == 9) or (i == 19) or (i == 29) or (i == 39):
        print(str(i))
    else:
        print(str(i) + " ", end = '')
