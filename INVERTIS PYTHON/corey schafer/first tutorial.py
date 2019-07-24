sms='como estas'
print(sms)
#here above there is no issue

#in case i write it as
#sms='como's estass
print(sms)
'''
it is an error to escape it we can write it within double
qutote or use \
'''

sms='como\'estas'
print(sms)


#instead use double quotes

sms="como estas"
print(sms)
'''
this doesn't mean that double quotes are better it goes
both ways
if i have to use double quotes in my sms then i will have
to use single quotes in my sms
'''

sms=' hala madrid "icist paris"'
print(sms)
#this is the wrong approach given below
#sms=" hala madrid "como estas""

sms=""" this is the moment we won't forget
we are blessed with the best bounties of the nature
we have to be more human we are doing something wrong"""
print(sms)



#to find the length of the string
sms="hola vamos"
print(len(sms))


print(sms[3])
#length of string at it starts with 0 sms[3] means
#starting from 0 the character at index 3





#this is string slicing

#all the characters between beginning and upto  but not including
#the last one
print(sms[:4])


