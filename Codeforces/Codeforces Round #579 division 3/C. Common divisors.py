q=int(input())
array=list(map(int,input().split()))
count=0
flag=[]
divisor=[]

for i in array:
    for j in range(1,i+1):
        if i%j==0:
            divisor.append(j)

from collections import Counter

dictionary=Counter(divisor)


solution=0
for key, value in dictionary.items(): 
	if value==len(array):
	  solution+=1
    

print(solution)

    
