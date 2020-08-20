class Settings:
	"""A class to store all settings for Alien Invasion """
	def __init__(self):
		"""Initialized the gams's setting"""
		# Screen setting
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255,255,250)

		# Ship setting
		self.ship_speed = 1.5
		self.ship_limit = 3

		# Bullet setting
		self.bullet_speed = 2
		self.bullet_width = 10
		self.bullet_height = 10
		self.bullet_color = (250,189,46)
		self.bullet_allowed = 3

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0 
		self.alien_speed = 1.0

	# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		
	def increse_speed(self):
		"""Increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale


		
		