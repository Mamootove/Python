class player:
    def __init__(self, hp, power, location):
        self.hp = hp
        self.power = power
        self.location = location
    def location(self):
        return (self.location)
    def power(self):
        return self.power
    def hp(self):
        return self.hp



player1 = player(150, 105, "x, y, z")
player2 = player(100, 20, ("x, y, z"))

h ="head"
b = "body"
f = "foot"
m = "miss"
n = 1
shoots = [h, b, m, b, f, m, m, m]
while player1.hp > 0:
    for shoot in shoots:
        print(shoot)
        if shoot == h:
            player1.hp -= 20
        elif shoot == b:
            player1.hp -= 10
        elif shoot == f:
            player1.hp-= 5
        print(player1.hp)

if player1.hp<=0:
    print("hp is zero, your fucked up")
    print("dead as nigga!")
