first=int(input("Enter the first number"))
last=int(input("Enter the last number of the given range"))


flag=0

for i in range(first,last+1):
    if i==1:
        continue

    flag=1

    for j in range(2,i//2 +  1):
        if(i%j==0):
            flag=0
            break

    if(flag==1):
        print(i,end=' ')


