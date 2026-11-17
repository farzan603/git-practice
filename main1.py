
arr = [10, 20, 5, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest number does not exist")
else:
    print("Second Largest Number:", second_largest)



print("Hello, World!")
print("Welcome to Python Programming")


