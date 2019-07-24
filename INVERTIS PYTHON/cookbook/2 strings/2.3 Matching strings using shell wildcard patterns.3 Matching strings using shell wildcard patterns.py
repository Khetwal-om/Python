'''
   matching strings using shell wildcard
   patterns
'''
print("hi")
from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat4.csv','Dat[0-9]*'))


'''
fnmatch matches patterns using same-
case sensivity rules as that of underlying
file system 
# On OS X (Mac) 
 fnmatch('foo.txt', '*.TXT') 
 False
 # On Windows fnmatch('foo.txt', '*.TXT') True 
fnmatchcase compares actual cases
'''



addresses=[
'5412 N CLARK ST',
    '1060 W ADDISON ST',  
  '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
'4802 N BROADWAY',
]

from fnmatch import fnmatchcase
output=[addr for addr in addresses if fnmatchcase(addr,'*ST')]
print(output)