import pickle
import datetime

with open("users.txt", "rb") as data:
    data = pickle.load(data)
import pickle


def _security():
    log = []
    while True:
        username = input("Enter your user name: ")
        password = input("Enter your password: ")

        if (username, password) in data.items():
            print("Access OK!")
            return True
        else:
            print("Username or password are incorrect")
            log.append(f"{username}, {datetime.datetime.now()}")
            cont = input("Do you wanna continue? (y/n) ")
            if cont.lower().startswith('y'):
                continue
            else:
                print("Crashed")
                return print(log), False

                


_security()

