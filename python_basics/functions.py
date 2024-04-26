#POSTIONAL FUNCTION:
def add_numbers(a,b):                 
  return a+b

result=add_numbers(3,5)
print(result)


#DEFAULT FUNCTION:
def greet(name="World"):
  print("Hello,"+name+"!")
greet()
greet("Spoorthi")


#KEYWORD FUNCTION:
def greet(name,greeting):
  print(greeting+","+name+"!")
greet(greeting="Hello",name="Spoorthi")


#ARBITARY FUNCTION(ARYS):
def multiply(*args):                     
  result=1
  for num in args:
    result*=num
  return result
print(multiply(2,3,4,5,6))


#ARBITARY FUNCTION(KWARGS):
def student_info(**kwargs):
  for key,value in kwargs.items():
    print(key+":"+value)
student_info(name="Spoorthi",age="20",clg="BITM")

L=[1,2,3]
print(L)
print(*L)




