def add():
    return a+b
def sub():
    return a-b
def mul():
    return a*b
def div():
    if b!=0:
        return a/b
    else:
        print("It Is Not Divisible By Zero")

print("add ,sub ,mul ,div")
choose=input("Enter your choice:")

a=float(input())
b=float(input())

if(choose=="add"):
   print("Result:",add())
elif(choose=="sub"):
    print("Result:",sub())
elif(choose=="mul"):
    print("Result:",mul())
elif(choose=="div"):
    print("Result:",div())
else:
    print("invalid input")
    
    
