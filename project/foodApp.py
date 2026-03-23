from login import Login


class Food:
    def start(self):
        print("<< Welcome To FoodApp >>")

        entry = Login()

        while True:
            for option in Login.loginMode:
                print(f"{option}.{Login.loginMode[option]}",end="   ")
            print()
            try:
                choice = int(input("Enter Your Choice : "))
                entry.Validate(Login.loginMode[choice])
            except ValueError:
                print("Invalid Choice Retry")
            except KeyError:
                print("Invalid Choice Retry")
                
            
            
Food().start()
