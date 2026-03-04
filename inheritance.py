class GrandParent:
    def native(self):
        print("Tamil Nadu")
#Single Inheritance
class Father():   #Parent Class
    def worth(self):
        print(100000)
class son(Father):    #Child Class 
    def run(self):
        print("running")
child1 = son()
child1.worth()
child1.run()
#Multiple Inheritance

class daughter(GrandParent,Father):
    def dance(self):
        print("Dance")
rose = daughter()
rose.dance()
rose.native()
rose.worth()
#Multilevel Inheritance
class Mother(GrandParent):
    def cook(self):
        print("Cooking")
class daughter2(Mother):
    def swim(self):
        print("swim")
raji = daughter2()
raji.cook()
raji.native()
raji.swim()
#Hierarchical Inheritance
class brother(Father):
    def school(self):
        print("Schooling")
class sister(Father):
    def college(self):
        print("college")
ram = brother()
rani = sister()
ram.school()
ram.worth()
rani.college()
rani.worth()