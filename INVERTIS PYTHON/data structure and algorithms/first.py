'''
algorithms: how to systematically perform a task
computing gcd(m,n)

step 1:list out factors of m
step 2:list out factors of n
step 3:identify the largest common factors

this code simply gives the factors of both the numbers
a=5
b=15
mylist_a=[]
mylist_b=[]
for i in range(1,5):
    if 5%i==0:
        mylist_a.append(i)

for i in range(1,10):
    if 15%i==0:
        mylist_b.append(i)

print(mylist_a)
print(mylist_b)

use mylist_a for list of factors of m
use mylist_b for list of factors of n

for each i from 1to m,add i if i divides m
for each j from 1to n,add j if j divides n
use commmon factor
for each f in mylist_a , add f in common if it is in mylist_b


return the common[-1] value

a=14
b=63
mylist_a=[]
mylist_b=[]
for i in range(1,a+1):
    if a%i==0:
        mylist_a.append(i)

for i in range(1,b+1):
    if b%i==0:
        mylist_b.append(i)

print(mylist_a)
print(mylist_b)

common=[]
for i in mylist_a:
    for k in mylist_b:
        if i==k:
            common.append(i)

print(common)
print("The LCM is",common[-1])

#i got a new approach
def lcm(a,b):
    common=[]
    for i in range(1,min(a,b)+1):
        if a%i==0 and  b%i==0:
            common.append(i)

    return common[-1]


print(lcm(11,77))





#further optimization
#we don't need the list

#mrcf most recent common factor is must


def gcd(m,n):
    mrcf=0
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mrcf=i

    return mrcf

print(gcd(11,9))


'''
#we should start from last



def gcd(m,n):
    i=min(m,n)
    while(i>0):
        if m%i==0 and n%i==0:
            return i
        else:
            i=i-1

print(gcd(4,16))
