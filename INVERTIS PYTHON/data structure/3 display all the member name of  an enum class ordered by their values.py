import enum
class Country(enum.IntEnum):
    india=7
    argentina=10
    france=11
    brazil=9
    spain=4


print('country name ordered by the country code')
print('\n'.join(''+data.name for data in sorted(Country)))
