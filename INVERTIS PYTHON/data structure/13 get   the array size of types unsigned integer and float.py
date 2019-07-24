from array import array
vamos=array("i",(1,2,3,4,5))
print(vamos.itemsize)
for data in vamos:
    print(data)
    print(type(data))




print("-------------")
hola=array("f",(12.24,234.2,23.4))
print(hola.itemsize)
for data in hola:
    print(data)
    print(type(data))







print(type(vamos))
print(type(hola))
