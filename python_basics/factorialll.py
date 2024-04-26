#FIBONACCI SERIES
n=int(input("Enter the value:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


#FUNCTION:
def factorial(n):
  if(n==1):
    return(1)
  else:
    return(n*factorial(n-1))
num=8
result=factorial(num)
print("factorial of",num,"is",result)