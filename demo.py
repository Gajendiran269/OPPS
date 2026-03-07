class Veh:  #Class
    brand = None    
    model = None    #Static Variable
   
    def __init__(self,num):     #Constructor
         self.num = num     #Instance Variable

    def run(self):  #Function
        print(f'{self.brand}  {self.model}  {self.num} is running successfully')
        
car = Veh(909)  #Object
car.brand = "Tata"
car.model = "mini"
car.run()