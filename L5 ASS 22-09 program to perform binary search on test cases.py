#A.pavan kumar 121910313047
# Program to perform binary search with Testcases

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

def test(arr,key):
    if arr!=sorted(arr):
        print("Array is not sorted, cannot implement binary search")
        return
    ans = binary(arr,key,0,len(arr)-1)
    if ans!=-1: print("The element", key, "is found at index", ans)
    else: print("The element", key, "is not found")

# Binary Search with test cases

# Test case 1 , sorted array with element present
print("TEST CASE 1")
arr1 = [1,2,3,4,5,6,7,8,9,10] # sorted array
key1 = 5 # present key
test(arr1,key1)

# Test case 2 , sorted array with element not present
print("TEST CASE 2")
arr2 = [1,2,3,4,5,6,7,8,9,10] # sorted array
key2 = 78 # not present key
test(arr2,key2)

# Test case 3 , unsorted array with element present
print("TEST CASE 3")
arr3 = [3,2,13,4,5,61,7,80,45,7] # sorted array
key3 = 5 # present key
test(arr3,key3)
