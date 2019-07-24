n=int(input("Enter the number"))
k=2*n-1

for i in range(1,n+1):
    for j in range(1,k+1):
        if (j==n):
            answer=96+i
            print(chr(answer),end="")
        else:
            print(" ",end="")
       

        if((j==n-1) or (j==n+1)):
            ans=64+i
            print(chr(ans),end="")

        if((j==n-2) or (j==n+2)):
            ans=96+i
            print(chr(ans),end="")

        if((j==n-3) or (j==n+3)):
            ans=64+i
            print(chr(ans),end="")


        if((j==n-4) or (j==n+4)):
            ans=96+i
            print(chr(ans),end="")
            
    print("\r")


