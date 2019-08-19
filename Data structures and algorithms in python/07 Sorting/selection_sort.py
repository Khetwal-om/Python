array=[43,34,5]
def selection(array):
    for i in range(len(array)-1):
        minIndex=i
        for j in range(i+1,len(array)):
            if array[j]<array[minIndex]:
                minIndex=j
            if i!=minIndex:
                array[i],array[minIndex]=array[minIndex],array[i]
    print(array)       

selection(array)
