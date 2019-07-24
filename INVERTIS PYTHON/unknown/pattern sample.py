n=5
k=n*2-1
for i in range(1,n+1):
    for j in range(1,k+1):

        if(j==n):
            print(chr(96+i),end="")
        else:
            print(" ",end="")


        if(j==n-1 or j==n+1):
            print(chr(64+i),end="")
        else:
            print(" ",end="")

        
        if(j==n-2 or j==n+2):
            print(chr(96+i),end="")
        else:
            print(" ",end="")

        
        if(j==n-3 or j==n+3):
            print(chr(64+i),end="")
        else:
            print(" ",end="")
        
        
        if(j==n-4 or j==n+4):
            print(chr(64+i),end="")
        else:
            print(" ",end="")
        

       
        

    print()

