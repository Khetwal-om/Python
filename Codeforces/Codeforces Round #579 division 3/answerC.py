count=0

import math
def gcd(m,n):
    if m<n:
        m,n=n,m
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
    
n=int(input())
data=list(map(int,input().split()))


n=len(data)
result=data[0]
for i in range(1,n-1):
    result=gcd(result,data[i])
    
    
for i in range(1,result+1):
    if result%i==0:
        count+=1
        if (i!=(result//i)):
            count+=1;
    
print(count)