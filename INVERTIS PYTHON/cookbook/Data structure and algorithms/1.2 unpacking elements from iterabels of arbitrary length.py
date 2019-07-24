def drop_first_last(grades):
    first,*middle,last=grades
    return avg(middle)


grades=int(input("Enter the grades"))
print(drop_first_last(grades))
