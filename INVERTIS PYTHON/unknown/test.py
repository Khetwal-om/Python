class Student:

	def setName(self,name):
		self.name=name

	def getName(self):
		return self.name


objeto=Student()
objeto.setName("Harry")
print(objeto.getName())

a=input("Enter anything")
print(a)