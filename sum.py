
n = int(input("Enter array size: "))

arr1 = []
arr2 = []
sum_array = []

print("Enter first array elements:")
for i in range(n):
    arr1.append(int(input()))

print("Enter second array elements:")
for i in range(n):
    arr2.append(int(input()))

# Add two arrays
for i in range(n):
    sum_array.append(arr1[i] + arr2[i])

print("Sum of two arrays:", sum_array)
