import pickle
import datetime

with open("users.txt", "rb")as data:
    data = pickle.load(data)
    
data = dict(data)
def inputer_log():
    user_name = input("Enter you username: ")
    password = input("Enter you password: ")
    return user_name, password
logs = []
counter_pass =0
def check_log(user_name, password):
    if user_name in data.keys():
        logs.append(datetime.datetime.now())
        if password == data[user_name]:
            print("Access successfully!!")
            
        else:
            print("oops! It was incorrect.")
            main()
            counter_pass += 1
            if counter_pass > 5:
                print("Your might be a Hacker!\nHere is 5min Timeout!")
                #Do something to make timeout
                
    else:
        print("The user name is not in DB!") #It gives additional information so avoid writing something like this!
        counter_pass += 1
        main()
    print(counter_pass)
        
def main():
    check_log(*inputer_log())
    
main()