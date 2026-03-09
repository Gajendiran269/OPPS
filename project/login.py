class Login:
    loginMode = {1:"LOGIN",
                 2:"SIGNUP",
                 3:"GUEST",
                 4:"EXIT"}
    
    def Login(self):
        print("Login")

    def Signup():
        pass
    
    def Guest():
        pass
    
    def Validate(self,choice):
        if choice == 1:
            self.Login()
        elif choice == 2:
            self.Signup()
        elif choice == 3:
            self.Guest()
        elif choice == 4:
            exit()
        else:
            print("Invalid Choice Retry")
    