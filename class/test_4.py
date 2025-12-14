class zoo:
    def __init__(self, zoo_name, zoo_location):
        self.zoo_name = zoo_name
        self.zoo_location = zoo_location
    def infos(self):
        return f'Its {self.zoo_name} in {self.zoo_location}'
    
zoo_eram = zoo("Eram", "Tehran")

class animals(zoo):
    def __init__(self, name, species, age, sound, zoo_name, zoo_location):
        self.name = name 
        self.species = species
        self.age = age 
        self.sound = sound
        self.zoo_name = zoo_name
        self.zoo_location = zoo_location

    def sounds(self):
        print(f'{self.sound}')

    def info(self):
        print(f"Its {self.name}, a {self.species}, {self.age} years young")

class bird(animals):
    def __init__(self, name, species, age, sound, wing_span, zoo_name, zoo_location):
        self.name = name 
        self.species = species
        self.age = age 
        self.sound = sound
        self.wing_span = wing_span
        self.zoo_name = zoo_name
        self.zoo_location = zoo_location

    def wing(self):
        print(f"wing span is {self.wing_span}")
    
    def sounds(self):
        print(f"{self.sound}"*10)



zoo_eram = zoo("Eram", "Tehran")
lion = animals("Yashar", "Cat", 22, "MEOOOWWWWW", "Eram", "Tehran")
pigeon = bird("Nigga", 'bird', 0.5, "JIK JIK", 18, "Eram", "Tehran")
