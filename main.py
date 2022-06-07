# select random number
x = int(input("Number:"))
print()

# number of loops
y = 0

# every number
evr = []

# even numbers
even = []

# odd numbers
odd = []

# create the loop
while x != 1:
    if x % 2 == 0:
        evr.append(int(x))
        even.append(int(x))
        x = x / 2
        y = y + 1

    else:
        evr.append(int(x))
        odd.append(int(x))
        x = 3 * x + 1
        y = y + 1

# convert the  "evr" list into numbers on a different row
for num in evr:
    print(num)

difference = len(even) - len(odd)

print(f"\n{y} loops")
print(f"The largest number is {max(evr)}")
print(f"\nThe odd ones are: \n{odd}")
print(f"\nThe even ones are: \n{even}")
print(f"\nThe even ones are {difference} more than the odd ones")
