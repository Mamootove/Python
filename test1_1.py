def starter():
    print("welcome to this game")
    print("guess a number between n1 and n2")
    print("You can write n1 and n2")
    n1 = int(input("The first number(n1): "))
    n2 = int(input("The second number(n2): "))
    return n1, n2
    

def computer_guess():
    from random import randint
    n1 = int(input("The first number(n1): "))
    n2 = int(input("The second number(n2): "))
    com_gs = randint(n1, n2)
    return com_gs


def guesss():
    gs = int(input("Make a guess: "))
    return gs


def play():
    if guesss() < computer_guess():
        print("Your number is samller")
    else:
        print("your number is bigger")


def ending(ans):
    print("Oh, What a guess[you dumb ass]")
    ans = input("do you wanna play again?(y,n) ")
    if ans == "y" or ans == 'Y':
        guess != computer
    elif ans =='N'or ans=='n':
        guess == computer
        print("Thanks for palying!")    



starter()
computer_guess()
guesss()

while guesss!=computer_guess:
    computer_guess()
    guesss()
    play()
ending()




