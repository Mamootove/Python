#Functions are here!!!
def take_name():
    '''
    Get user name and  surname, Then retuns them.
    '''
    name = input("Tell me your name: ")
    sur = input("Tell me your last name: ")
    return name, sur

def len_name(name, sur):
    '''
    just make len of st and then return it and it's len.
    '''
    ln = len(name)
    ls = len(sur)
    return name, sur, ln, ls

def khoshgelesh_kon(name, sur, ln, ls):
    '''
    Prints using f-string and match the name with it len. 
    '''
    print(f"Name: {name}, len: {ln}")
    print(f"Surname: {sur}, len: {ls}")
    print(f"{name} {sur}, total: {ln+ ls}")

def rate_hour():
    '''
    A liitle more complicated than others!
    get 2 inputes and multiplies them 
    if even one of the inputes isn't int, it give you an error with the describtion that where it happend.  
    '''
    hour = input("How many hour do you work a day? ")
    rate = input("How much do you earn in an hour? ")
    a = True
    b = True
    try:
        hour = int(hour)
    except:
        print("There is an issue with the hour input")
        a = False
        rate_hour()
    try:
        rate = int(rate)
    except:
        print("There is an issue with the rate input")
        b = False
        rate_hour()
    if a and b ==True:
        print(f"you earn {hour * rate} daily")

khoshgelesh_kon(*len_name(*take_name()))
print("___________________________________")
rate_hour()


    
    
