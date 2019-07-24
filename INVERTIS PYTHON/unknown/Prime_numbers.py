i,j,flag=0,0,0
first=int(input("Enter the number"))
last=int(input("Enter the last number"))


# Traverse each number in the interval
# with the help of for loop
for i in range(first, last + 1):

# Skip 1 as1 is niether
# prime nor composite
    if (i == 1):
        continue

# flag variable to tell
# if i is prime or not
    flag = 1

    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break

    if (flag == 1):
        print(i,end=' ')


# flag = 1 means i is prime
# and flag = 0 means i is not prime



