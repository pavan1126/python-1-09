#A.pavan kumar 121910313047
# Program to perform linear search

# Initialisation of  array

arr = [1,23,4,5,6,8,4,2,5,7,332,5,6,7,4,55,79,4,5]

# Taking the element to input from user
key = int(input("Enter the element to search : "))
found = False
index = None

# Logic for linear search
i = 0
while i<len(arr):
    if arr[i]==key:
        found = True
        index = i
        break
    i+=1

# Printing the result
if found: print("The element", key, "is found at index", index)
else: print("The element is not found")
