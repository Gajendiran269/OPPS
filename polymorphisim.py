#Compile Time
class Student:
    def __init__(self,name,year):
        self.Name = name
        self.Year = year
    def classTime(self,timing = 0,start = None,end = None):
        if start is not None and end is not None:
            print("class time is",end - start)
        else:
            print("class time is",timing)
student1 = Student("ashok",4)
student1.classTime(9)
#Runtime
class Parent:
    def Drive(self):
        print("Parent drives")
class Child(Parent):
    def Drive(self):
        print("Child drives")

obj = None
inp = input()
if inp =="Parent":
    obj = Parent()
else:
    obj = Child()
obj.Drive()