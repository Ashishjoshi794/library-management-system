# OOP => Object Oriented Programming
# OOP is completely based on classes and objects

# Class is a blueprint to create the objects
# The structures to build a object is defined in the class

# Objects are the instances of a class 

# Multiple objects can be created using a single class

# OOP has 4 most important pillars
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction

# Attributes => The variables defined inside the class
# Methods => Functions defined inside the class
# Method always has a self parameter


# Defining a class
# class keyword is used to define a class
# Syntax to define a class
# class class_name:
#     properties(attributes or methods)

# TO create a object from a class, we need to call the class
# obj_name = class_name()


# class Students:
#     name = "Ujjwal Neupane"
    
#     def abc(self): # Method always contains self parameter at first
#         print(self)
#         print(" I am displaying abc")

# s1 = Students()

# print(s1.name)
# s1.abc()
# print(s1)
# print()
# print()
# s2 = Students()
# print(s2.name)
# s2.abc()
# print(s2)
# print()
# print()
# s3 = Students()
# print(s3.name)
# s3.abc()
# print(s3)


# Class Attributes
# The value of attributes doesnot changes according to the object


# Object Attributes
# The value of attribute changes according to the object
# To create the object attribute,
# we need a method to set the values for the attributes


class Students:

    college_name = "Mindrisers College"
    
    def set_info(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        # print(f"COllege Name = {self.college_name}")
        print()
        print()
        
    def abc(self):
        print("Displaying abc")
        
s1 = Students()
s1.set_info("Ujjwal Neupane",27, "Male")
s1.abc()
print()
s1.display()



        
s2 = Students()
s2.set_info("Ram Neupane",26, "Male")
s2.abc()
print()
s2.display()


        
s3= Students()
s3.set_info("Sita Neupane",28, "Female")
s3.abc()
print()
s3.display()



# name = "Ujjwal Neupane"
# print(type(name))

# del => Deletes the attributes or methods from the class

del Students.college_name
del s1.name

s1.display()

s1.abc()