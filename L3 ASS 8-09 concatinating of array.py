#121910313047 A.pavan kumar
#concatinating of array
n=int(input("Enter number of elements in first array :"))
a=[]
for i in range(0,n):
  value=int(input("Enter number :"))
  a.append(value)
m=int(input("Enter number of elements in second array :"))
b=[]
for j in range(0,m):
  value=int(input("Enter number :"))
  b.append(value)
print(a+b)

