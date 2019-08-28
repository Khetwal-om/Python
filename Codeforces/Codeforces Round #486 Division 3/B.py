n=int(input())
pal=[]
for i in range(n):
    string=input()
    pal.append(string)
pal.sort(key=len)
minIndex=0
flag=0
for i in range(len(pal)):
    for j in range(i+1,len(pal)):
        if pal[minIndex] not in pal [i+1]:
            flag=1
            break
    minIndex+=1
    
if flag==0:
    print("YES")
    for i in pal:
        print(i)
else:
    print("NO")