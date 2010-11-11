# Ran|Ship: Item() class.
import Object

class Item(Object.Object):
    def __init__(self, **values):
        super(Item, self).__init__(values)
        self.value = values['value']
        self.condition = values['condition']
    
    def is_broken(self):
        if self.condition <= 0: return True
        else: return False
    
    def is_sellable(self):
        if self.value >= 1: return True
        else: return False
    
    def add_damage(self, dmg):
        self.condition -= dmg
        if self.condition < 0: self.condition = 0
    
    def heal_damage(self, dmg):
        self.condition += dmg
        if self.condition < 100: self.condition = 100
    
