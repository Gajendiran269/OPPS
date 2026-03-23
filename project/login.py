from Models.user import User
from Models.userManager import userManager
class Login:
    loginMode = {1:"login",
                 2:"signup",
                 3:"guest",
                 4:"exit"}
    
    def login(self):
        Mail  = input("Enter mail:")
        Password  = input("Enter Password:")

        user = userManager.getUsers(Mail,Password)  
        if user:
            print(f"Welcome {user.Name}")
        else:
            print("Invalid Credentials")
    
    def signup(self):
        Name  = input("Enter Name:")
        Number  = int(input("Enter Number:"))
        Mail  = input("Enter mail:")
        Password  = input("Enter Password:")

        user = User(Name, Number, Mail, Password)    
        userManager.addUser(user)


    
    def guest(self):
        print("guest")

    def exit_app(self):
        print("Thank You For Using FoodApp")
        exit()
    
    def Validate(self, choice):
        method_name = self.loginMode.get(choice)
        if method_name:
            getattr(self, method_name)()
        else:
            print("Invalid Choice Retry")
    #     if choice == 1:
    #         self.Login()
    #     elif choice == 2:
    #         self.Signup()
    #     elif choice == 3:
    #         self.Guest()
    #     elif choice == 4:
    #         print("Thank You For Using FoodApp")
    #         exit()
    #     else:
    #         print("Invalid Choice Retry")
    