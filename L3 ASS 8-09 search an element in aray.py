#121910313047 A.pavan kumar
#search an element in an array
def search(x,n):
  for i in range(0,n):
    if(a[i] == x):
      return (i+1)
      break;

n=int(input("Enter length of array : "))
a=[]
for j in range(0,n):
  value = int(input("Enter element : "))
  a.append(value)

x=int(input("Enter a search element : "))
res=0
res=search(x,n)
print(x," is found in ",res," position")
