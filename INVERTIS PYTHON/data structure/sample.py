from enum import Enum
Direction=Enum('Direction','North East South West')
print(type(Direction))
print(list(Direction))


print('-------------')
print(list(Direction.__members__.values()))
print('-------------')
print(list(Direction.__members__.items()))

for data in Direction:
    print(data)


strdirection=Enum('strdirection',{"North":"N","East":"E",
                                  "South":"S","West":"S"})

print(list(strdirection))



print(strdirection.North==strdirection.South)
print(strdirection.East==strdirection.East)
print(strdirection.West==strdirection.West)


print(Direction["North"])
print(id(Direction.North))
print(id(Direction["North"]))


print(Direction(1))
print(Direction(2))
print(Direction(3))
print(Direction(4))


class Colour(Enum):
    Red=1
    Blue=3
    Green=4

print(Colour.Red)



class Timezone:
    def __init__(self,offset,dst):
        self.offset=offset
        self.dst=dst
    def earlier_than(self,other):
        #ignoring dst
        return self.offset<other.offset
    def
