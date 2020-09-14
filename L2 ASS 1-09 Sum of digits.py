#A.pavan kumar - 121910313047
# Program on sum of digits of number and armstrong number
a = int(input("Enter a number: "))  
sum = 0
sum2 = 0
b = a  
  
while(a!=0):
     rem = a%10
     sum = sum + (rem**3)
     sum2 = sum2 + rem
     a = a//10
  
if (sum == b):  
   print("is an Armstrong number")  
else:  
   print("is not an Armstrong number")

#sum of digits is

print("sum of digits is",sum2)
