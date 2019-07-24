'''
def gcd(m,n):
    i=min(m,n)


    while(i>0):
        if (m%i)==0 and (n%i)==0:
            return i
        else:
            i=i-1

#how is this
#for i in range(1,min(m,n)+1)
'''

'''
#i am considering m>n
def gcd(m,n):
    if n>m:
        (m,n)=(n,m)


    if m%n==0:
        return n

    else:

        diff=m-n
        return gcd(max(n,diff),min(n,diff))


    
    
'''
#again euclid's algorithm

def gcd(m,n):
    if m<n:
        (m,n)=(n,m):
    while m%n!=0:
        diff=m-n
        (m,n)=gcd(max(diff,n),min(diff,n))

    return n
