#GCD and LCM of three numbers
x=int(input("Enter a value:"))
y=int(input("Enter b value:"))
z=int(input("Enter c value:"))

#logic for GCD
if(x<y) and (x<z):
    small=x
elif(y<x) and (y<z):
    small=y
else:
    small=z
for i in range(1,small+1):
    if(x%i==0 and y%i==0 and z%i==0):
        gcf=i

#logic for LCM
lcm=(x*y*z)/gcf

#Displaying GCD nad LCM of two numbers
print("GCM of x and y and z is",gcf)
print("LCM of x and y and z is",lcm)
