from collections import Counter
def compare(n1,n2):
    return Counter(n1)==Counter(n2)
list_a=[1,2,3,4,5]
list_b=[1,2,3,4,5]
print(compare(list_a,list_b))


