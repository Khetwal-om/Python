
n=int(input())
array=[]
for i in range(n):
    element=int(input())
    array.append(element)
    

for i in range(len(array)):
	print(array[i])
print('--------')
for i in range(0,len(array)):
    if array[i]>array[i+1]:
        temp=array[i+1]
        array[i+1]=array[i]
        array[i]=temp
        
        
print(array)

t=int(input(""))
for i in range(t):
    c=[]
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        
        s=(a[i]*20)-(b[i]*10)
        c.append(s)
        
    if max(c)>0:
        print(max(c))
    else:
        print(0)