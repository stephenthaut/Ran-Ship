# Ran|Ship: Object() class.

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
    
