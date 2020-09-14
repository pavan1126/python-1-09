#GCD and LCM of two numbers
a=int(input("Enter x value:"))
b=int(input("Enter y value:"))

#logic for GCD
if(x<y):
    small=x
else:
    small=y
for i in range(1,small+1):
    if(x%i==0 and y%i==0):
        gcf=i

#logic for LCM
lcm=(x*y)/gcf

#Displaying GCD nad LCM of two numbers
print("GCM of x and y is",gcf)
print("LCM of x and y is",lcm)
