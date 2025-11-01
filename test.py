from random import randint
print("welcome to the guessing game!!\nYou can choose 2 numbers and I choose one between them, Then you guess that")
c = True
b = True
n1 = int(input("The first number: "))
n2 = int(input("The second number: "))
count = 0
while c:
    a = randint(n1, n2)
    while b:
        count += 1
        vorodi = int(input("Your guess? "))
        if vorodi !=a:
            if vorodi > a:
                print("Your number is bigger")
            elif vorodi < a:
                print("Your number is smaller")    
            
        else:
            b = False
            print(f"Wow, The number was {vorodi}, you guessed it in {count} tries!! , How did you knew it??")
            replay = input("Wanna Play Another Round?:(Y,N) ")
            if replay.upper()== "Y":
                c =True
            elif replay.upper() in ['N','NO', 'NAH']:
                c = False
                print("Thanks for playing")