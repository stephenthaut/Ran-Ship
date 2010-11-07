# Ran|Ship: Object(object).

class Object(object):
    """ Base object for all other objects in Ran|Ship."""
    def __init__(self, tag, name, description, contents=[]):
        """ Assign variables from arguments."""
        self.tag = tag
        self.name = name
        self.description = description
        self.contents = contents
    
    def __str__(self):
        """ Return a str() description of the object."""
        return "%(n)s: %(d)s" % {'n':self.name, 'd':self.description}
    
    def search_contents(self, item_tag):
        """ Search self.contents, return an index if item exists."""
        if item_tag in [i.tag for i in self.contents]: return True
        else: return False
    
    def open_container(self):
        """ Pass items from self.contents to caller, empty self.contents."""
        for item in self.contents: yield item
        self.contents = []
    
