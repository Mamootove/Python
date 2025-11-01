def list_odd(l):
    o=[x for x in l if x % 2==1]
    return o, len(o)
print(list_odd([1,2,5,4,6,8,79,48]))
def hello_world():
    print("Hello, world!")
hello_world()

def greet():
    name = input("Enter Your Name: ")
    print(f"Hello, {name}!")
greet()
def is_positive():
    number = int(input("What is Your number? "))
    if number >= 0:
        print(True)
    else:
        print(False)
is_positive()
def sum_of_squares():
    a = int(input("your first number? "))
    b = int(input("your second number? "))
    print(a**2+b**2)
sum_of_squares()
def is_even():
    n = int(input("number? "))
    if n %2==0:
        res = (True)
    else:
        res = (False)
    print(res)
is_even()
def is_greater():
    a= int(input("first: "))
    b = int(input("second: "))
    if a > b:
        res = True
    else:
        res = False
    print(res)
is_greater()
def sum_infinit(*args):
    res = 0
    for i in args:
        res += i
    print(res)
sum_infinit(5,4,8,88,66565,584,548,0,102)
def pick_evens(*args):
    even = []
    for i in args:
        if i %2 ==0:
            even.append(i)
    print(even)
pick_evens(1,2,3,5,4,6,5,9,8,5,4,55,5,5454,54,45487,9,798)
def skyline(*args):
    tallest = 0
    for _ in args:
        if _ > tallest:
            tallest = _
    print(tallest)
skyline(1,1,1,1,1,0)

