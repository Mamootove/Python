import datetime

def timer(f):
    def wrraper(*a):
        now = datetime.datetime.now()
        f(*a)
        then = datetime.datetime.now()
        df = then - now 
        print(df)
    return wrraper
