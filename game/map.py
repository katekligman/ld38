class Map(object):

	def __init__(self, name, width, height):

		self.name = name
		self.width = width
		self.height = height
		self.terrains = []
		self.creatures = []


	def add_terrain(self, terrain):

		if self.is_valid(terrain):
			self.terrains.append(terrain)
		else:
			raise Exception("Cant add")

	def add_creature(self, creature):

		if self.is_valid(creature, x, y):
			self.creatures.append(creature)
		else:
			raise Exception("Cant add")

	def is_valid(self, sprite):

		# Checks if there's collision
		for t in terrains:
			if sprite.check_collision(t):
				return False

		for c in creatures:
			if sprite.check_collision(c,):
				return False

		if not self.in_map(sprite):
			return False

		return True

	def in_map(self, sprite):

		if (0 <= sprite.x  and sprite.x <= self.width) and (0  <= sprite.y and sprite.y <= self.height):
			return True

		return False
