from collections import defaultdict
roll=[('v',1),('vi',3)]

nova=defaultdict(list)

for k,v in roll:
    nova[k].append(v)

print(sorted(nova.items()))
