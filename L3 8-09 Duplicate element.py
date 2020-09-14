# Python code to remove duplicate elements 
def Remove(duplicate): 
    final=[] 
    for num in duplicate: 
        if num not in final: 
            final.append(num) 
    return final 
duplicate = [1,2,4,5,3,2,3,5,8,9] 
a=Remove(duplicate) 
print("elements of the array after removing duplicates is")
for i in range(0,len(a)):
    print(a[i])
print("and array is:",a)
