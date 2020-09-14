#121910313047 A.pavan kumar
#coping one array to another array
arr1 = [1,2,3,4,5];
arr2 = [None]*len(arr1)

#coping arr1 to arr2
for i in range(0,len(arr1)):
  arr2[i] = arr1[i];

print("Elements of original array :",arr1)
print("Elements of copied array :",arr2)
