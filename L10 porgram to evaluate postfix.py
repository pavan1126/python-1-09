#A.pavan kuamr - 121910313047
#  program to evaluate postfix expression
def postfix(exp):
    s=[]
    for i in exp:
        if i.isdigit():
            s.append(int(i))
        elif i == "+":
            a = s.pop()
            b = s.pop()
            s.append(int(a)+int(b))
        elif i == "-":
            a = s.pop()
            b = s.pop()
            s.append(int(b)-int(a))
        elif i == "*":
            a = s.pop()
            b = s.pop()
            s.append(int(a)*int(b))
        elif i == "/":
            a = s.pop()
            b = s.pop()
            s.append(int(b)/int(a))
    return s.pop()
exp = input("Enter an expression:")
val = postfix(exp)
print("Required value is : ")
print(val)
