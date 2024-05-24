pi = 3.14

class Shape:
	def __init__(self) -> None:
		pass
	def __str__(self) -> str:
		return f"{self.colour.title()} {self.shape.title()}; X: {self.x}, Y: {self.y}, Z: {self.z}."

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





# -------------------------------------------------------------------------------------------------------------------------------------------
def main():
	cube = Shape_crs_sect("Cube", "Red", 10, 9, 8)

if __name__	== "main":
    main()