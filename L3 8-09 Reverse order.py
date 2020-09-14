#copying elements from one array to another array in reverse order
a=[1,2,3,4,5]
b=[None]*len(a)
length=len(a)
#logic starts here
for i in range(0,length):
    b[i]=a[length-i-1]
#printing output
print("the elements of first array is")
for i in range(0,length):
    print(a[i])
print("the elements of reversed array is",b)
for i in range(0,len(b)):
    print(b[i])
