# Ran|Ship
# Game objects.
import random, string

# Base-level classes.
class Object(object):
    """Create a basic Object() class for other classes to inherit from."""
    def __init__(self, **values):
        self.ship = values['ship']
        self.tag  = values['tag']
        self.name = values['name']
        self.description = values['description']
        self.contents = values['contents']
    
    def __str__(self):
        """Return a string description of the object."""
        return "%(n)s: %(d)s" % {'n':self.name, 'd': self.description}
    
    def add(self, lst, tag):
        """Add tag to list."""
        self.__dict__[lst].append(tag)
    
    def rm(self, lst, tag):
        """Remove tag from list."""
        self.__dict__[lst].remove(tag)
    
    def check(self, lst, tag):
        """Check if tag is in list."""
        if tag in self.__dict__[lst]: return True
        else: return False
    
    def take(self, lst, tag):
        """Take tag from list."""
        if self.check(lst, tag):
            return self.__dict__[lst].pop(self.__dict__[lst].index(tag))
        else: return False
    
    def access(self, tag):
        """Access object from ship."""
        return self.ship.access_object(tag)
    
    def search(self, func):
        """Search objects in ship."""
        return self.ship.search_objects(func)
    
    def delete(self, tag):
        """Delete object from ship."""
        return self.ship.delete_object(tag)
    

class Ship(object):
    """Create the Ship object as a catalogue of objects."""
    def __init__(self):
        self.keylist = list(string.letters[:26])
        self.objects = {}
    
    def generate_tag(self):
        """Generate a random tag from 456,976 possibilities."""
        key = ''.join(random.choice(self.keygen) for n in range(4))
        return "[%(k)s]" % {'k':key}
    
    def add_object(self, tag, the_object):
        """Add an object to self.objects."""
        self.objects[tag] = the_object
    
    def access_object(self, tag):
        """Return an object from the catalogue."""
        if tag in self.objects: return self.objects[tag]
        else: return False
    
    def search_objects(self, func):
        """Return objects from the catalogue that respond to func."""
        return [
            self.objects[o].tag for o in self.objects if func(self.objects[o])
        ]
    
    def delete_object(self, tag):
        """Delete an object from the catalogue."""
        if tag in self.objects: 
            del self.objects[tag]
            return True
        else: return False
    


# Classes inheriting from Object.
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
    



