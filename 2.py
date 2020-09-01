# Lcm of two numbers
a = int(input())
b = int(input())

if(a > b ):    
    max= a
else:
    max= b
while(True):
    if(max % a == 0 and max % b == 0):   
        print(max)
        break;
    max= max+ 1

