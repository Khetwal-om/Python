words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]


from collections import Counter

words_counts=Counter(words)
top=words_counts.most_common(10)
print(top)



count=Counter(words)
total=count.most_common(4)
print(total)
