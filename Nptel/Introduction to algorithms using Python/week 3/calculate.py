import time
start_time = time.time()

def selection_sort(a):
    for i in range(len(a)):
        minIndex=i
        for j in range(i,len(a)):
            if a[j]<a[minIndex]:
                minIndex=j
        a[i],a[minIndex]=a[minIndex],a[i]
        print(a)
                
        

list_a=list(range(400,1,-1))
selection_sort(list_a)
print(list_a)

print("--- %s seconds ---" % (time.time() - start_time))
