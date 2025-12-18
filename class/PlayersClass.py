
class user:
    def __init__(self, name, level, inventory, status):
        self.name = name
        self.level = level
        self.inventory = inventory
        self.status = status
    
    def level_up(self):
        self.level += 1
        self.status["hp"] += 10
        self.status["power"] += 50
        self.add_item()
        
    def add_item(self, item):
        self.inventory += [item]
    
    def delete(self, it, w):
        if w == 'inventory':
            try:
                self.inventory -= ["it"]
            except:
                print(f"There is no item called {it} in inventory!")
                
                
    def rs(self):
        print(f"player name:{self.name}, player Level:{self.level}, player inventory:{self.inventory}, player status:{self.status}")
            
    


