# Inheritance 
# Inheritance is the process of creating a new class from an existing class
# The child class can access the properties of parent class

# Types of Inheritance
# 1. Single Inheritance
# One Child class inherits from only one Parent class

# class Parent:
#     pass
#     # name = "Parent Class"
    
#     # def display(self):
#     #     print("I am displaying Parent class")
        
# class Child(Parent):
#     pass
#     # name = "Child Class"
#     # def display(self):
#     #     print("I am displaying Child class")
        
# c1 = Child()
# print(c1.name)
# c1.display()

# 2. Multiple Inheritance
# One child class inherits from multiple parent classes

# class Parent1:
#     pass
#     # name = "Parent Class 1"
    
#     # def display(self):
#     #     print("I am displaying Parent class 1")
        
# class Parent2:
#     pass
#     # name = "Parent Class 2"
#     # def display(self):
#     #     print("I am displaying Parent class 2")
        
# class Child(Parent1, Parent2):
#     pass
#     # name = "Child Class"
#     # def display(self):
#     #     print("I am displaying Child class")
        
# c1 = Child()
# print(c1.name)
# c1.display()

# MRO order => Method Resolution Order
# The order in which the parent classes are searched when a method is called on an object of
# MRO is always taken from class not from object
# print(class_name.mro())
# print(Child.mro())

# 3. Multilevel Inheritance
# One child class inherits from Parent class 
# Then the Parent class also inherits from GrandParent class
# So ultimately, the child class could access the propertief of both Parent class and GrandParent class also

# class GrandParent:
#     pass
#     # name = "Grand Parent Class"
    
#     # def display(self):
#     #     print("I am displaying Grand Parent class")
        
# class Parent(GrandParent):
#     pass
#     # name = "Parent Class"
    
#     # def display(self):
#     #     print("I am displaying Parent class")
        
# class Child(Parent):
#     pass
#     # name = "Child Class"
    
#     # def display(self):
#     #     print("I am displaying Child class")
        
# c1 = Child()
# print(Child.mro())
# print(c1.name)
# c1.display()

# Constructors
# Constructor is a special method that runs automatically when an object is created from a class
# There is only one constructor and that is __init__
# Constructor is mostly used for creating the object attributes

# class Students:
#     def __init__(self, name, age): # Constructor
#         self.name = name # Object attribute
#         self.age = age # Object attribute
        
#     def display(self):
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print()
        
# s1 = Students("Ujjwal Neupane", 27)
# s1.display()
# s2 = Students("Sujan Neupane", 25)
# s2.display()
# s3 = Students("Laxmi Neupane", 26)
# print(s3.name)
# print(s3.age)



# class GrandParent1:
#     pass
#     # name = "Grand Parent Class 1"
#     # def display(self):
#     #     print("I am displaying Grand Parent class 1")
        
# class GrandParent2:
#     pass
#     # name = "Grand Parent Class 2"
#     # def display(self):
#     #     print("I am displaying Grand Parent class 2")
        
# class Parent1(GrandParent1, GrandParent2):
#     pass
#     # name = "Parent Class 1"
#     # def display(self):
#     #     print("I am displaying Parent class 1")
        
# class Parent2:
#     pass
#     # name = "Parent Class 2"
#     # def display(self):
#     #     print("I am displaying Parent class 2")
        
# class Child(Parent1, Parent2):
#     pass
#     # name = "Child Class"
#     # def display(self):
#     #     print("I am displaying Child class")
        
# print(Child.mro())
# c1 = Child()
# print(c1.name)
# c1.display()

# class Child2(Parent1, Parent2):
#     name = "Child Class 2"
#     def display(self):
#         print("I am displaying Child class 2")


# super()
# super() is used to access the properties of parent class from within the child class 
# super() directly calls the method of parent class
# but in Python, super() callls the next class in MRO chain
# After the finishing of current methid of parent class, it fallback to the class from where it is being called

class A:
    def display(self):
        print("I am displaying A class")
        
class B(A):
    def display(self):
        super().display() # Accessing the display method of class A
        print("I am displaying B class")
        
class C(A):
    def display(self):
        super().display() # Accessing the display method of class A
        print("I am displaying C class")
        
class D(B, C):
    def display(self):
        super().display() # Accessing the display method of class B and C
        print("I am displaying D class")
        
print(D.mro())        
d = D()
d.display()