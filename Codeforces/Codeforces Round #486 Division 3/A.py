n,k=map(int,input().split())
students=list(map(int,input().split()))

count=0
indices=[]
flag=1
nova=[]

for i in students:
    if i not in nova:
        count+=1
        indices.append(flag)
        nova.append(i)
        if count==k:
            break
            
        
        
    flag+=1
    
        


        
if count>=k:
    print('YES')
    for i in indices:
        print(i,end=' ')
else:
    print('NO')