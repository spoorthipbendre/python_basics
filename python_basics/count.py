#COUNT DIGITS IN A NUMBER
num=19111103
count=0
while (num!=0):
    num//=10
    count+=1
print("Number of the digits:",str((count)))
