pi = 3.14

class Shape:
	def __init__(self, type, colour, x, y, z) -> None:
		self.type = type
		self.colour = colour
		self.x = x
		self.y = y
		self.z = z
	
	@property
	def shape(self):
		return self._shape
	
	@shape.setter
	def shape(self, shape):
		self._shape = shape

	@property
	def colour(self):
		return self._colour
	
	@colour.setter
	def colour(self, colour):
		# if colour not in []:
		self._colour = colour

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		self._y = y

	@property
	def z(self):
		return self._z

	@z.setter
	def z(self, z):
		self._z = z
	
	def getPos(self):
		return f"{self.colour} {self.type}; X: {self.x}, Y: {self.y}, Z: {self.z}."



# -------------------------------------------------------------------------------------------------------------------------------------------
def main():
	cube = Shape("Cube", "Red", 10, 9, 8)
	# cube = Shape("Cube", None, 10, 9, 8)
	print(cube.getPos())

if __name__	== "__main__":
	main()