from enum import Enum
class Country(Enum):
    india=4
    spain=7
    argentina=10
    brazil=11

for data in Country:
    print('{}       :{}'.format(data.name,data.value))
