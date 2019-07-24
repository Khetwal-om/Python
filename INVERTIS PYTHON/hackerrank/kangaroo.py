'''
if x1+v1==x2+v2:
    x1+=v1 
    print("YES")
else:
    print("NO")

'''
'''
x1=43
v1=2
kangA=[]
x2=70
v2=2
kangB=[]
for i in range(x1,100,v1):
    kangA.append(i)
for j in range(x2,100,v2):
    kangB.append(j)


print(kangA)
print(kangB)


if len(kangA)==len(kangB):
    for item in range(len(kangA)):
        for elements in range(len(kangB)):
            if kangA[item]==kangB[item]:
                print("YES")
                break;
        


elif len(kangA)<len(kangB):
    for item in range(len(kangA)):
        for elements in range(len(kangA)):
            if kangA[item]==kangB[item]:
                print("YES")
                break;


elif len(kangA)>len(kangB):
    for item in range(len(kangB)):
        for elements in range(len(kangB)):
            if kangA[item]==kangB[item]:
                print("YES")
                break;
        


        

'''

def kangaroo(x1, v1, x2, v2):
    kangA=[]
    kangB=[]
    if x2>x1 and v2>v1:
        print("In x2>x1 and v2>v1")
        return "NO"
    else:
        for i in range(x1,10000+1,v1):
            kangA.append(i)
        for j in range(x2,10000+1,v2):
            kangB.append(j)

        print("len of kangA",len(kangA))
        print("len of kangB",len(kangB))
        if len(kangA)==len(kangB):
            print("in equals comparison")
            for item in range(len(kangA)):
                for elements in range(len(kangB)):
                    if kangA[item]==kangB[item]:
                        print("YES")
                        break;
                return "NO"
        
        elif len(kangA)<len(kangB):
            print("IN smaller A than B")
            for item in range(len(kangA)):
                for elements in range(len(kangA)):
                    if kangA[item]==kangB[item]:
                        print("YES")
                        break;
                return "NO"


        elif len(kangA)>len(kangB):
            print("IN larger than B")
            for item in range(len(kangB)):
                for elements in range(len(kangB)):
                    if kangA[item]==kangB[item]:
                        print("YES")
                        break;
                return "NO"




x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
    




