#A.pavan kumar 121910313047
# Program to perform binary search with functions

def binary(arr,key,low,high):
    if high >= low: 
        mid = (high+low)//2
        if arr[mid]==key: 
            return mid 
        elif arr[mid]>key: 
            return binary(arr, key, low, mid-1) 
        else: 
            return binary(arr, key, mid+1, high) 
    else: 
        return -1


# Initialsing the array
arr = []
# Taking the element to input from user
size = int(input('Enter the size of the array : '))
print('Enter the elements of the array')
for i in range(size):
    arr.append(input())
key = input("Enter the element to search : ")

if arr!=sorted(arr):
    print("Array is not sorted, cannot implement binary search")
else:
    ans = binary(arr,key,0,len(arr)-1)
    if ans!=-1: print("The element", key, "is found at index", ans)
    else: print("The element", key, "is not found")
