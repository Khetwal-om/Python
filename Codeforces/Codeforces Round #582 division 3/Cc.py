n,m=input().split()
n=int(n)
m=int(m)


fact=[]
for i in range(1,n+1):
    if i%m==0:
        objeto=i%10
        fact.append(objeto)
        

print(sum(fact))
