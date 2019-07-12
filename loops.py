numbers = [2, 3, 5, 7]
for number in numbers:
    print(number)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))
