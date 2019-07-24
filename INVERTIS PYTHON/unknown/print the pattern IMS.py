A=[]
B=[]

n=int(input("Enter the number of elements of A "))
print("Enter the  elements of A ")
for i in range(1,n+1):
    element=int(input(""))
    A.append(element)



m=int(input("Enter the elements of B "))
print("Enter the  elements of B ")
for i in range(1,m+1):
    element=int(input(""))
    B.append(element)



print(A)
print(B)

C=A+B
#C.sort()
#print(",".join(str(C)))
#print(" ".join(sorted(list(set(C)))))
#print(" ".join(str(sorted(list(set(C)),reverse=True))))

print(" ".join(str(sorted(list(C),reverse=True))))


