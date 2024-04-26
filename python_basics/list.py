#LIST
#append()method
l=["abc",1,2,7,True,2.5]
l.append("bike")
print(l)

#insert()method
l[-1]="car"
l.insert(-2,"pens")
print(l)

#remove()method
l=["abc",1,2,7,True,2.5]
l.remove(True)
print(l)

#del()method
del l[-1]
print(l)