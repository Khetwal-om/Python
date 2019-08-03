number,k=input().split()
number=int(number)
k=int(k)

i=1

while i<=k:
    if number%10!=0:
        number=number-1
    else:
        number=number//10
    i=i+1

    
print(number)

