from random import randint
print("here is a guessing game!\nGive me a range and then I give you a random number from the choosen range and then you have to guess the random number")
#two numbers inputed-->
b = True
while b:
    n1=int(input("starting with? "))
    n2= int(input("ending with? "))
    a = randint(n1,n2)
    n = int(input(f'guess a number between {n1} and {n2}: '))
    if n == a:
        print('winner winner chicken dinner!')
        #when a=n : we can continue playing or exit the game
        replay= input("do you wanna play again?(y,n): ")
        if replay=="y" or replay== "Y":
            b = True
        elif replay=="n" or replay== "N":
            b = False
    else:
        print(f"The number was {a}, but try again later")