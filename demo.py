class Veh:  #Class
    brand = None    #Object
    model = None
    num = None
    def __init__(self,num):     #Constructor
         self.num = num

    def run(self):  #Function
        print(f'{self.brand}  {self.model}  is running successfully')
car = Veh(909)
car.brand = "Tata"
car.model = "mini"
car.run()