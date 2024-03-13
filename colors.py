class Colors:
		mint_green = (134,240,162)
		yellow = (253,253,150)
		orange = (255,195,110)
		darkpink = (255,161,156)
		lightpink = (255,209,220)
		blue = (193,193,243)
		purple = (238,203,255)
		darkblue = (84,143,139)
		green = (120,184,64)
		white = (255,255,255)

		# python decorator that allows you to define our method that can be called on our class rather than an instance
		@classmethod
		def get_cell_colors(cls):
			return [cls.mint_green,cls.darkpink,cls.yellow,cls.lightpink,cls.blue,cls.purple,cls.darkblue,cls.green]
			