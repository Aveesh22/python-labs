# Write the necessary code to print out the result of the following:
#	 	2 + 4 + 6 + 8 + 9 + 10 + 12 + 14 + 16 + 18

counter = 2
sum = 0
while(counter < 18) :
    sum += counter
    counter += 2
sum += 9
print(sum)