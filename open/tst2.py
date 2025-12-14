import pickle
import datetime

with open("users.txt", "rb") as data:
    data = pickle.load(data)
print(data)





def _security():
    def userer():
        user = input("Enter your user name: ")
        passw = input("Enter your password: ")
        return user, passw
    
    def checker(username, password):
        access = True
        while access:
            if (username, password) in data.items():
                print("Access OK!")
                access = False
            else:
                print("Username or pass are incorrect")
                cont = input("Do you wanna continue? ")
                if cont.lower()=='y':
                    _security()
                else:
                    access = False
                    print("Crashed")

    checker(*userer())



_security()

