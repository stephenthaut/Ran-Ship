# Ran|Ship: Container Class ("Container.py").

class Container(object):
	def __init__(self, variables):
		self.__dict__ = variables
	
# Testing:
# __init__()
TestContainer = Container({"name":"Test", "colour":"Red"})
print TestContainer.name   # => "Test"
print TestContainer.colour # => "Red"

# super_init()
class Thing(Container):
	def __init__(self, variables):
		super(Thing, self).__init__(variables)
	
	# Other function definitions ...

TestThing = Thing({"name":"Test 2", "colour":"Blue"})
print TestThing.name   # => "Test 2"
print TestThing.colour # => "Blue"