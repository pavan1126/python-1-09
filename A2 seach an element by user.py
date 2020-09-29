#search an element by given user
a=[]
n=int(input("length of an array :"))
print("Enter ",n, "items")
for i in range(0,n):
  value  = str(input())
  a.append(value)

x = str(int(input("Enter the search item :")))


for k in range(len(a)):
  if a[k] ==x:
    print("positin is :",k+1)
    break
