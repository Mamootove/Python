name = input("Enter your name: ")
sur = input("Enter your sur name: ")

ln = len(name)
ls = len(sur)
tot = ln + ls

print(f"{name} has {ln} characters!", end="***")
print(f"{sur} has {ls} characters!")
print(f"the total characters are {tot}")

print("________________________________________")

hour = int(input("How many hours do you work a day? "))
pay = int(input("How much do you earn an hour? "))
#Probably user work 22 days a month(not expecting thursdays and fridays)
money = hour * pay *22

print(f"you probably earn {money} monthly.")
