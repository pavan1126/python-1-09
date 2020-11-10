#A.pavan kumar - 121910313047
#program on finding the first and second smallest number
def Range(arr):    
    lowest = arr[0]  
    for x in arr[1:]:       
        if x < lowest:  
            low = lowest 
            lowest = x  
        elif low > x:  
            low = x  
               
    print("Smallest element is:", lowest)    
    print("Second Smallest element is:", low)  

arr = [12, 1, 2, 41, 31, 10, 8, 6, 4] 
Range(arr)
