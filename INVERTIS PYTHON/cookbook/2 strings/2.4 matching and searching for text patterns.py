#wanna search text for a specific pattern

text='yeah,this is it Zidane is back yeah'

print(text=='yeah')
print(text.startswith('yeah'))
print(text.endswith('yeah'))
print(text.find('is'))

#for more complicated patterns use re

text1='12/4/2018'
text2='June 12,2018'

import re
#  \d+ one or more digits
if re.match(r'\d+/\d+/\d+',text1):
	print("matched")
else:
	print('no')

if re.match(r'\d+/\d+/\d+',text2):
	print('yes')
else:
	print("this is not matched")

'''
If you’re going to perform a lot of matches 
using the same pattern,
 it usually
pays to precompile the regular expression
pattern into a pattern object first
 '''


date_pattern=re.compile(r'\d+/\d+/\d+')
if date_pattern.match(text1):
	print("matched")
else:
	print('no')


'''
match() always tries to find the match
 at the start of a string. 
If you want to search text for all 
occurrences of a pattern, use the findall() method instead.
'''

