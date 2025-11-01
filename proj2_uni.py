def take_name():
    name = input("Tell me your name: ")
    sur = input("Tell me your last name: ")
    return name, sur

def len_name(name, sur):
    ln = len(name)
    ls = len(sur)
    return name, sur, ln, ls

def khoshgelesh_kon(name, sur, ln, ls):
    print(f"Name: {name}, len: {ln}")
    print(f"Surname: {sur}, len: {ls}")
    print(f"{name} {sur}, total: {ln+ ls}")

def rate_hour():
    hour = input("How many hour do you work a day? ")
    rate = input("How much do you earn in an hour? ")
    a = True
    b = True
    try:
        hour = int(hour)
    except:
        print("There is an issue with the hour input")
        a = False
    try:
        rate = int(rate)
    except:
        print("There is an issue with the rate input")
        b = False
    if a and b ==True:
        print(f"you earn {hour * rate} daily")
    else:
        print("OY stupid!!")
    

khoshgelesh_kon(*len_name(*take_name()))
print("___________________________________")
rate_hour()


    
    
