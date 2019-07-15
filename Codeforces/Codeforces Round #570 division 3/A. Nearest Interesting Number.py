number=int(input())
temp=number

def interesting(number):
    addition=0
    remainder=0
    temp=number
    while(number!=0):
        remainder=number%10
        addition=addition+remainder
        number=number//10
    
    return addition%4

        
for i in range(temp,1100):
    if interesting(i)==0:
        print(i)
        break

