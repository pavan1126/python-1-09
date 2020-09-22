#A.pavan kumar 121910313047
# Program to perform binary search

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
arr = [1,23,4,5,6,8,4,2,5,7,332,5,6,7,4,55,79,4,5]
arr.sort()
# Taking the element to input from user
key = 100 # present in the array
ans = binary(arr,key,0,len(arr)-1)

if ans!=-1: print("The element", key, "is found at index", ans)
else: print("The element", key, "is not found")
    
