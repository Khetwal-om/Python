'''
count number of students
'''
from collections import Counter

batches=(
    ('first',1),
    ('second',4),
    ('third',29),
    ('first',34)
    )


students=Counter(batch_name for batch_name,no_students in batches)
print(students)
