import subprocess
def girande():
    num = int(input("Enter your number:\n"))
    argham = str(num)
    argham_l = len(argham)

    for i in argham:
        print(i ,int(i) * "* ")

    #even or odd checker:
    if argham_l % 2 ==0 and num % 2 == 0:
        print("blastoff")
    elif argham_l % 2 == 1 and num % 2 == 1:
        print("blastoff")


girande()
