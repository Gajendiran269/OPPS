from Models.user import User
from Models.userManager import userManager
class Login:
    loginMode = {1:"LOGIN",
                 2:"SIGNUP",
                 3:"GUEST",
                 4:"EXIT"}
    
    def Login(self):
        Mail  = input("Enter mail:")
        Password  = input("Enter Password:")

        user = userManager.getUsers(Mail,Password)  
        if user:
            print(f"Welcome {user.Name}")
        else:
                print("Invalid Credentials")
    def Signup(self):
        Name  = input("Enter Name:")
        Number  = int(input("Enter Number:"))
        Mail  = input("Enter mail:")
        Password  = input("Enter Password:")

        user = User(Name, Number, Mail, Password)    
        userManager.addUser(user)


    
    def Guest(self):
        print("guest")
    
    def Validate(self,choice):
        if choice == 1:
            self.Login()
        elif choice == 2:
            self.Signup()
        elif choice == 3:
            self.Guest()
        elif choice == 4:
            print("Thank You For Using FoodApp")
            exit()
        else:
            print("Invalid Choice Retry")
    