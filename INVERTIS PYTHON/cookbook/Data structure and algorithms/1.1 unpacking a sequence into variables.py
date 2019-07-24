mylist=["Real Madrid","camp nou","parc des princes"]
a,b,c=mylist
print(a)
print(b)
print(c)
'''
Real Madrid
camp nou
parc des princes
'''
mytuple=('prevaricate','indolent')
x,y=mytuple
print(x,y)

'''
Real Madrid
camp nou
parc des princes
prevaricate indolent
'''

data=['eastside',40,(2019,3,12)]
l,m,date=data
print(l,m,date)
print("This is the date tuple separated to an individual variable",date)
'''
Real Madrid
camp nou
parc des princes
prevaricate indolent
eastside 40 (2019, 3, 12)
'''

'''
Real Madrid
camp nou
parc des princes
prevaricate indolent
eastside 40 (2019, 3, 12)
This is the date tuple separated to an individual variable (2019, 3, 12)
'''
year,month,day=date
print("------------------")
print(year,"/",month,"/",day)
'''
This is the date tuple separated to an individual variable (2019, 3, 12)
------------------
2019 / 3 / 12'''


#can also discard some of the code


_,check,_=date
print(check)

