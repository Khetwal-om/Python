from enum import IntEnum
class Country(IntEnum):
    india=7
    france=9
    brazil=10
    spain=4
    germany=11



country_code=list(map(int,Country))

print(country_code)
