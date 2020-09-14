#121910313047 A.pavan kumar
#Deleting duplicate elements from user values
a=[]
n= int(input("Enter the number of elements :"))
for i in range(0,n):
    element=int(input())
    a.append(element)
b = set()
unique = []
for i in a:
    if i not in b:
        unique.append(i)
        b.add(i)
print("original elements:")
print(unique)
