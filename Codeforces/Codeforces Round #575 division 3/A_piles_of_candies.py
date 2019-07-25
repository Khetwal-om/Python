def solution(a,b,c):
    difference=0
    alice=a
    bob=b
    left=c
    variation=a-b
    c=c-variation
    bob=bob+variation
    
    
    if c%2==0:    
        alice=alice+c//2
        bob=bob+c//2
 
    else:
        alice=alice+c//2
        bob=bob+c//2
        if alice>bob:
            difference=alice-bob
            print(difference)
            alice=alice-difference
        else:
            difference=bob-alice
            print()
            bob=bob-difference
            
            
            
    alice=alice-difference
    bob=bob-difference
    
    return bob
    

q=int(input())
for i in range(q):

    a,b,c=input().split(' ')
    a=int(a)
    b=int(b)
    c=int(c)
    if a>=b and (a-b)<=c:
        #print("1 Yes,proceed in a>b and (a-b)<c")
        print(solution(a,b,c))
    elif a>=c and (a-c)<=b:
        #print("2 Yes,proceed in elif of a>c and (a-c)<b")
        print(solution(a,c,b))
    elif b>=a and (b-a)<=c:
        #print("3 b>a and (b-a)<c case")
        print(solution(b,a,c))
    elif b>=c and (c-b)<=a:
        #print("4 b>c and (b-c)<a case")
        print(solution(b,c,a))
    elif c>=a and (c-a)<=b:
        #print("5 c>a and (c-a)>b")
        print(solution(c,a,b))
    elif c>=b and (c-b)<=a:
        #print("6 c>b and (c-b)>b")
        print(solution(c,b,a))
