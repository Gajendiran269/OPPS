from Models.user import User
class userManager:
    __Users = []
    @classmethod
    def addUser(cls,user):
        if isinstance(user,User):
            cls.__Users.append(user)
            print("User Added Successfully",user.Name)
        else:
            print("Invalid User")
    @classmethod
    def getUsers(cls,mail,password):
        for user in cls.__Users:
            if user.Mail == mail and user.Password == password:
                return user
        
