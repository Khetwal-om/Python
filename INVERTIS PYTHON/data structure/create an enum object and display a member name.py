from enum import Enum
class Country(Enum):
    india=23;
    spain=7;
    france=11;
    italy=10;
    england=10;


print('name of the member{}'.format(Country.india.name))
print('this is the id{}'.format(Country.india.value))

print('another one{}'.format(Country.spain.value))
print('another value{}'.format(Country.spain.name))



print('here is the boss'.format(Country.france.name));
print('here is the value'.format(Country.france.value));


print('come to the premier league{}'.format(Country.england.name));
print('yes england{}'.format(Country.england.value));



print('cr7 comes to juventus{}'.format(Country.italy.name))
print('cr7 is the ultimate boss{}'.format(Country.italy.value));
