#A.pavan kumar 121910313047
# Program to perform linear search with functions

# Function for linear search
def linear(key,arr):
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
    else: print("The element", key, "is not found")
    
# Initialsing the array
ar = []

# Taking the inputs from the user
size = int(input('Enter the size of the array : '))
print('Enter the elements of the array')
for i in range(size):
    ar.append(input())
key = input("Enter the element to search : ")
linear(key,ar)
