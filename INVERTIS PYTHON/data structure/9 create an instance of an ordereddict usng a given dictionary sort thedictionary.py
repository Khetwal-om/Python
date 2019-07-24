from collections import OrderedDict
dict={'india':7,'spain':11,'france':10}

new_dictionary=OrderedDict(dict.items())

for key in new_dictionary:
    print(key,new_dictionary[key])


print("now reverse order")


for key in reversed(new_dictionary):
    print(key,new_dictionary[key])
