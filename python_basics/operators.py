#Operators(NOT)
a=20
a=~20
print(a)

a=-20
a=~20
print(-a)

#operations(XOR)
a=5
b=7
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#Operators(AND)
a=20
if(a&1==0):                   #for odd condition (a&1==1)
    print("EVEN")
else:
    print("ODD")
    
a=int(input("Enter the value a:"))
b=int(input("Enter the value b:"))
c=int(input("Enter the value c:"))
if(a>b and a>c):
    print("a is greater than b and c.")
elif(b>a and b>c):
    print("b is grater than a and c.")
else:
    print("c is grater than a and b.")

