Instance variable
object level variables
by using self(within the class) or by using 
object reference (outside of class)

STATIC VARIABLE:
-------------------------
class level variables
directly,by using cls variable
by using class name of outside of the class


LOCAL VARIABLE:
-------------------
method level variable
we should not use self,cls,classname


#from the class we can access global variables directly within the method of a class we can declare global variables by using global


class Test:
 def me():
  a=100
  print(a)

 def me():
  b=100
  print(b)

t=Test()
t.m1()
t.m2()

We can't access local variables outside of the class


#this is valid


class Test:
 def me():
  a=100
  print(a)

 def me():
  b=100
  a=43
  print(b)
  print(a)

t=Test()
t.m1()
t.m2()  


#2
class Test:
def average(self,list):
   result=sum(list)
   print(result)

t.Test()
t.average([10,20])





#global variable
x=100
class Test:
   def m(self):
       print(x)

t=Test()
t.m()





#
x=10
class Test:
    x=777
    def m1(self):
       print(x)
       print(self.x)   #this print's static one
    def m2(self):
        print(x)
        print(Test.x)


t=Test()
t.m1()
t.m2()




#This is the global x

class Test:
   def m1(self):
       global x
       x=888
       print(x)

    def m2(self):
       print(x)

#this won't show the error as x is declared to be global

#Instance method,Getter and Setter
Types
Instance methods
class methods
static methods


Instance methods:
--------------------

setter and getter methods:
----------------------------------
  


#s.name= direct access no validation
#s.getName() with validation
#hiding data behind methods----encapsulation


class Employee:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

aaj tak 
zee news
uttaranchal
aastha

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n=int(input("Number of students"))
for i in range(n):
    name=input("Name")
    marks=int(input("marks"))
    s=Employee()
    s.setName(name)
    s.setMarks(marks)

    print("Hola ",s.getName()," your marks are",s.getMarks())



#s.name= direct access no validation
#s.getName() with validation
#hiding data behind methods----encapsulation




Difference between instance method and
class method .

Outside the class we can call instance method only using the object reference.
First we have to create object,unless we
are not using instance variable we shouldn''t really make a object to call it.


To declare instance method:

def m(self):
   pass

To declare class method:

def m(cls):   #cls is class level variable
   print(cls.name)

 #whatever static variables are made can be
 #accessed

 difference between self and cls:

 self is referencing to current object,
 while cls is referencing to current class object.

self instance variable
cls static or class level variable


2 In class method decorator is needed @classmethod but in instance method nothing is needed as such


3. Inside class method we are able to access only class variable,while within instance method we can access both instance variable as well as static variable.


INSTANCE VS CLASS
1. Inside method body if we are using atleast one instance variable then
 we should declare that method as instance method

2.Inside method body if we are using only static variable ,we must declare method as
class method.

3  In class method decorator is needed @classmethod but in instance method nothing is needed as such...


4 The first argument to the instance method should be self and by using self,this is reference to current object we can acces instance variables inside method..
The first argument to the classmethod should be cls which is reference variable current class object and by using that we can access static variables.

4.Inside instance method we can access both instance and static variables Inside classmethod we can access only static variables and we can't access instance variables.


5. We can call instance method by using object reference.
We can call classmethod either by using object reference as well as class name but recommended to use classname

 

#dangal
#kasauti 




class Animal:
    legs=2;

    @classmethod
    def data(cls,name):
        print("The name of the animal is{} and it have {} legs".format(name,cls.legs))


#No need to create the object of the class
Animal.data('kangaroo')
Animal.data('Penguin')



---------------------

class Maths:
    count=0

    def __init__(self):
        Maths.count+=1

    @classmethod
    def objects_number(cls):
        print("The number of objects created are",cls.count)



objetoA=Maths()
objetoB=Maths()
objetoC=Maths()
objetoD=Maths()
objetoE=Maths()
Maths.objects_number()






 #Static Method explanation

It's a general utility methods/helper methods

@staticmethod
def sum(x,y):
    print("The sum is",x+y)

Can call using object reference as well as class name(recommended)


class Student:
    @staticmethod
    def add(x,y):
        print("sum",x+y)

    @staticmethod
    def product(x,y):
        print("Product",x*y)

    @staticmethod
    def average(x,y):
        print("Average",(x+y)/2)



#no static variable no instance variable

Student.add(10,2)
Student.product(10,2)
Student.average(10,2)

!If we are using any instance varaibles inside method body then we should go for instance method .We should call using obj
reference.
2.If we are only using static variables inside method body then this method no way related to particular object.We should declare such type of methods as classmethod
Calling is done by using object reference or using class name(recommended)
3.If we are using any instance variable and any static variable inside method body,
to define such type of general utility methods we should go for static methods.
Calling is done using obj reference or class name(recommended)

#If we are not using any decorator :
------------------------------------------
For classmethod ,@classmethod decorator is mandatory.
For staticmethod,@staticmethod decorator is optional.

Without any decorator method can be either instance method or static method.
If we are calling 

If calling using object-Instance method
If calling using class name-Static method





--------------------------
class Test:
    def hola(x):
        print(x*10)
        print("This is just to test method without decorator")


Test.hola(12)

class Test:
    def m1(self):
        print("some method")

t=Test()
t.m1()
# Python will consider method as instance method,
# but we are not declaring self variable.Hence error
# occurs





Valid code . This is static method
class Test:
    def m():
        print("some method")

Test.m()


No confusion if decorator is provided,without it there is no confusion

class Test:
    @staticmethod
    def m():
        print("some method")

Test.m()





www.[IMS-GHAZIABAD.AV.IN(technotsav2019)]
9560913611


Garbage collection

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

#destructor

__del__(self):
This will be used to execute database collection,network collection
Just before destroying an object garbage collector calls destructor.
For every class is object,that object class destructor will be called


import time
class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

objeto=Clean()
time.sleep(4)
 

 import time
class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

objeto=Clean()
time.sleep(4)
print("end of app")
---------------------------------------
This is calling of the constructor
end of app
This performs cleanup activities
---------------------------------------

#after end of app garbage collection will work
'''
This is calling of the constructor
end of app
This performs cleanup activities
'''




#difference
This is calling of the constructor
This performs cleanup activities
end of app




class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

objeto=Clean()
objeto=None #This object doesn't refers to anyone so first gc removes this
time.sleep(4)
print("end of app")










----------------------------------

class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

objeto=Clean()
print(objeto)
objeto=None #This object doesn't refers to anyone so first gc removes this
time.sleep(4)
print(objeto)
print("end of app")



#if we don't wanna make objeto available




class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

objeto=Clean()
print(objeto)
del objeto #This object doesn't refers to anyone so first gc removes this
time.sleep(4)
print(objeto)#NameError: name 'objeto' is not defined
print("end of app")






import time 
import gc
class Clean:
    def __init__(self):
        print("This is calling of the constructor")

    def __del__(self):
        print("This performs cleanup activities")

gc.disable() #in classes this won't work because gc is very sensitive to classes
print(gc.isenabled())
t1=Test()
t1=None
time.sleep(10)
print("End ")

THE PURPOSE OF DESTRUCTOR IS TO PERFORM CLEANUP ACTIVITIES BEFORE DESTROYING AN OBJECT.


import time
# class Clean:
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
# objeto=Clean()
# time.sleep(4)
# print("end of app")
#after end of app garbage collection will work
'''
This is calling of the constructor
end of app
This performs cleanup activities
'''
#
#
#
# class Clean:
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
# objeto=Clean()
# print(objeto)
# objeto=None #This object doesn't refers to anyone so first gc removes this
# time.sleep(4)
# print(objeto)
# print("end of app")
#


#if we don't wanna make objeto available

#
#
#
# class Clean:
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
# objeto=Clean()
# print(objeto)
# del objeto #This object doesn't refers to anyone so first gc removes this
# time.sleep(4)
# # print(objeto)#NameError: name 'objeto' is not defined
# print("end of app")
#


'''-----------------------------------'''
# class Test:
#
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")

#
# objetoA=Test()
# b=objetoA
# c=b
# d=c

'''
Single object all other are references to it
objetoA=None This object is still not available for garbage collection
t2=None still can't be used by gc
c,d should also go for the eligibility of garbage collection
'''





#
# class Test:
#
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
#
# t1=Test()
# t2=t1
# t3=t2
# t4=t3
# del t1
# time.sleep(2)
# print("After deleting t1 is not destroyed")
# del t2
# del t3
# print("Still not destroyed")
# del t4
# time.sleep(2)
# print("End of application")



# '''-----------------------------'''
# class Test:
#
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
# list=[Test(),Test(),Test()]
# time.sleep(1)
#
# print("End of application")
'''
This is calling of the constructor
This is calling of the constructor
This is calling of the constructor
End of application
This performs cleanup activities
This performs cleanup activities
This performs cleanup activities
'''















#
# class Test:
#
#     def __init__(self):
#         print("This is calling of the constructor")
#
#     def __del__(self):
#         print("This performs cleanup activities")
#
# list=[Test(),Test(),Test()]
# time.sleep(1)
# list=None
print("End of application")

'''
This is calling of the constructor
This is calling of the constructor
This is calling of the constructor
This performs cleanup activities
This performs cleanup activities
This performs cleanup activities
End of application
'''

import sys
class Check:
    def __init__(self):
        print("initialisation of object")

t1=Check()
t2=t1
t3=t2
print(sys.getrefcount(t1))
'''4 ref count t1,t2,t3 explicit
               self implicit
               '''
