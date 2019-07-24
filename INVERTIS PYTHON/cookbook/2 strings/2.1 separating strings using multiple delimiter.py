import re
line='''
Almost every useful program1involves some kind of
text7processing, whether it is parsing data
or8generating output. This9chapter focuses on
'''

fields=re.split(r'[0-9]',line)


values=fields[::2]
delimiters=fields[1::2]+['']
print(values)
print(delimiters)

print(''.join(a+b for a,b in zip(values,delimiters)))
