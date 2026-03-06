class Bank:
    def __init__(self):
        self.accName = None    #public
        self._accNum = None   #protected
        self.__accBal = None    #private
    #Setter
    def setData(self,Name,Num,Bal):
        if len(Name) < 4:
            print("Invaid Name")
        else:
            self.accName = Name
        self._accNum = Num
        self.__accBal = Bal
    #Getter
    def getData(self):
        return (self.accName, self._accNum, self.__accBal)
bank = Bank()
bank.setData("Arun",90909,78000)

print(bank.getData())
    
#Setter and Getter
class Book:
    def __init__(self):
        self._Name = None
    @property
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self,name):
        self._Name = name

book = Book()
book.Name = "Harry potter"
print(book.Name)