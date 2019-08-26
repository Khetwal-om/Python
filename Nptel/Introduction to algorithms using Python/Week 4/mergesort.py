def merge(A,B):
    C=[]
    m=len(A)
    n=len(B)
    i=0
    j=0
    
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>=B[j]:
            C.append(B[j])
            j+=1
    return C

def mergesort(A,left,right):
    #sort the slice A[left:right]
    if right-left<=1:  #base case
        return A[left:right]
    if right-left>1:  #recursive call
        mid=(left+right)//2
        L=mergesort(A,left,mid)
        R=mergesort(A,mid,right)
        
        return merge(L,R)

print('hola')
A=list(range(1,100000,2))+list(range(1,100000,3))
print(mergesort(A,1,len(A)))
    