numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
3
print(numbers[-1])
2
print(numbers[3])
1
print(numbers[:-1])
[3, 1, 4, 1, 5, 9]
print(numbers[3:4])
[1]
print(5 in numbers)
True
print(7 in numbers)
False
print("3" in numbers)
False
print(numbers + [6, 5, 3])
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Change the first element of numbers to "ten"
numbers[0] = "ten"
print(numbers[0])
# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers[-1])
# Get all the elements from numbers except the first two
numbers[2:]
print(numbers)
# Check if 9 is an element of numbers
9 in numbers
print(9 in numbers)