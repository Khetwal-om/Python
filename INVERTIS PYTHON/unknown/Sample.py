class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def display(self):
        print("Fervor :intense feelign of excitement",self.name,self.color)



name=input("Enter name of dog")
color=input("Enter the color of dog")

our=Dog(name,color)
our.display()
