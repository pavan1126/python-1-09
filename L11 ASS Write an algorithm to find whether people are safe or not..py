#A.pavan kumar - 121910313047
#program on Write an algorithm to find whether people are safe or not.
A = input("Enter the string: ")
flag = 1
count = 0
stack = []
for x in A:
   if x == "(":
       stack.append(x)
   if x == ")":
       if stack == []:
           flag = 0
           break
       Y = stack.pop()
       if Y != "(":
           flag = 0
           break
       else:
           count = count+1            
if flag == 1:
   print("Count: %d" %(count))
else:
   print("-1")
