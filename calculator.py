def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div (a,b):
    return a/b
def calulator():
    op=int(input("enter \n1:+\n2:-\n3:*\n4:/"))
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    if op==1:
        print(add(a,b))
    elif op==2:
        print(sub(a,b))
    elif op==3:
        print(mul(a,b))
    elif op==4:
        print(div(a,b))
    else:
        print("Error")  
print(calulator())             