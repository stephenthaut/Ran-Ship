# Ran|Ship: Ship() class.
import random
from string import letters

class Ship(object):
    """Create the Ship object as a catalogue of objects."""
    def __init__(self):
        self.keylist = list(letters[:26])
        self.objects = {}
    
    def generate_tag(self):
        """Generate a random tag from 456,976 possibilities."""
        key = ''.join(random.choice(self.keygen) for n in range(4))
        return "[%(k)s]" % {'k':key}
    
    def add_object(self, the_object):
        """Add an object to self.objects."""
        tag = self.generate_tag()
        self.objects[tag] = the_object
        return tag
    
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
    

