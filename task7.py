def mylist():
    x=int(input("enter the first number="))
    y=int(input("enter the second number="))
    z=x+y
    print("the addition of two numbers=",z)
    z=x-y
    print("the subtraction of two numbers=",z)
    z=x*y
    print("the multiplication of two numbers=",z)
    z=x//y
    print("the division of two numbers=",z)
mylist()
#add sub
def arthi(x,y):
    c=x+y
    d=x-y
    a=x*y
    b=x/y
    return c,d,a,b
result1, result2,result3,result4=arthi(10,2)
print(result1,'\n',result2 ,'\n',result3 ,'\n',result4 ,'\n')


#function covid
x=input("enter the covid patient name:")
x=98
if(x!=98):
    print("enter the body temperature:",numb)
else:
    print("the body temp is=98")


#fun covid
x=input("enter the patient name:")
def covid():
    print("The patient body tempature is:98")
covid()