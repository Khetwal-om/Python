def is_leap(year):
    leap = False
    
    if ((year%4==0) and (year%100==0) and (year%400==0)):
        leap=False
        print("in first")
    if ((year%4==0)and (year%100==0)):
        print("in second")
        leap=True
    return leap

year=int(input("Enter the year"))
print(is_leap(year))
