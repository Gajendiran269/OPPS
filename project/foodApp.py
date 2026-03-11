from login import Login


class Food:
    def start():
        print("<< Welcome To FoodApp >>")

        entry = Login()

        while True:
            for option in Login.loginMode:
                print(f"{option}.{Login.loginMode[option]}",end="   ")
            print()
            try:
                choice = int(input("Enter Your Choice : "))
                entry.Validate(choice)
            except ValueError:
                print("Invalid Choice Retry")
                
            
            
Food.start()
