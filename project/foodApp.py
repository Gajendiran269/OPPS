from login import Login


class Food:
    def start():
        print("<< Welcome To FoodApp >>")

        for option in Login.loginMode:
            print(f"{option}.{Login.loginMode[option]}",end="   ")
            print()
        choice = int(input("Enter Your Choice : "))
        entry = Login()
        entry.Validate(choice)
Food.start()
