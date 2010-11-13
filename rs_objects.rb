# Ran|Ship: rs_objects.rb (Game container classes).
=begin
	Container classes implemented in Ran|Ship:
	- Item() ! [name, items, cond, value]
		- Room(Item) ! [name, items, cond, value, doors, exits, chars]
		- Door(Item) ! [name, items, cond, value, open, lock, breakable]
		- Lock(Item) ! [name, items, cond, value, type, key, locked]
		- Body(Item) ! [name, items, cond, value, parts]
		- Part(Item) ! [name, items, cond, value, edible, damage_type]
		- Weap(Item) ! [name, items, cond, value, type, damage, ammo]
		- Char(Item) ! [name, items, cond, value, body, weap]
			- Enemy(Char)  ! [name, items, cond, value, body, weap, weakness, fixed, range]
			- Friend(Char) ! [name, items, cond, value, body, weap, speech]
			- Player(Char) ! [name, items, cond, value, body, weap]
=end

class Item 
	attr_reader :name, :items, :cond, :value
	def initialize name, items, cond, value 
		@name, @items, @cond, @value = name, items, cond, value
	end
	def add_item item 
		@items << item
	end
	def rem_item item 
		@items.delete item
	end
	def find_item item 
		@items.index item
	end
	def take_damage int, type 
		@cond -= int
		@cond = 0 if @cond < 0
	end
	def heal_damage int, type 
		@cond += int
		@cond = 100 if @cond > 100
	end
end
class Room < Item 
	attr_reader :name, :items, :cond, :value, :doors, :exits, :chars
	def initialize name, items, cond, value, doors, exits, chars
		super
		@doors, @exits, @chars = doors, exits, chars
	end
	def check_direction dir
		if @exits.key? dir then @doors[dir] else false end
	end
end
class Door < Item 
	attr_reader :name, :items, :cond, :value, :open, :lock, :breakable
	def initialize name, items, cond, value, open, lock, breakable
		super
		@open, @lock, @breakable = open, lock, breakable
	end
	def take_damage int, type
		super if @breakable
		@open = false if @cond == 0	
	end
	def heal_damage int, type
		super if @breakable
		@open = true if @cond > 0
	end
	def unlock key
		@open = true if @lock.unlock key
	end
end
class Lock < Item 
	attr_reader :name, :items, :cond, :value, :type, :key, :locked
	def initialize name, items, cond, value, type, key, locked
		super
		@type, @key, @locked = type, key, locked
	end
	def unlock key
		case key.class
		when String then @locked = false if @key == key
		when Item   then @locked = false if @key.name == key
		end
	end
end
class Body < Item 
	attr_reader :name, :items, :cond, :value, :parts
	def initialize name, items, cond, value, parts
		super
		@parts = parts
	end
	def select_damaged_part type
		parts = @parts.reject {|part| part.damage_type != type}
		parts[rand(parts.length)]
	end	
	def take_damage int, type
		part = select_damaged_part type
		part.take_damage(int, type)
	end
	def heal_damage int, type
		part = select_damaged_part type
		part.take_damage(int, type)
	end
end
class Part < Item 
	attr_reader :name, :items, :cond, :value, :edible, :damage_type
	def initialize name, items, cond, value, edible, damage_type
		super
		@edible, @damage_type = edible, damage_type
	end
end
class Weap < Item 
	attr_reader :name, :items, :cond, :value, :type, :damage, :ammo
	def initialize name, items, cond, value, type, damage, ammo
		super
		@type, @damage, @ammo = type, damage, ammo
	end
	def calc_damage
		(@damage[0]..@damage[1]).to_a[rand(@damage[1] - @damage[0])]
	end
end
class Char < Item 
	attr_reader :name, :items, :cond, :value, :body, :weap
	def initialize name, items, cond, value, body, weap
		super
		@body, @weap = body, weap
	end
	def take_damage int, type
		@body.take_damage int, type
	end
	def heal_damage int, type
		@body.heal_damage int, type
	end
end
class Enemy < Char 
	attr_reader :name, :items, :cond, :value, :body, :weap, :weakness, :fixed, :range
	def initialize name, items, cond, value, body, weap, weakness, fixed, range
		super
		@weakness, @fixed, @range = weakness, fixed, range
	end
	def calc_damage
		@weap.calc_damage
	end
end
class Friend < Char 
	attr_reader :name, :items, :cond, :value, :body, :weap, :speech
	def initialize name, items, cond, value, body, weap, speech
		super
		@speech = speech
	end
	def speek
		@speech
	end
end
class Player < Char 
	attr_reader :name, :items, :cond, :value, :body, :weap
	def initialize name, items, cond, value, body, weap
		super
	end
end
