from re import S


class Student:
	def __init__(self, name, house):
		# self.name = name
		# self.house = house
		# if not name:
		# 	raise ValueError("Name is required.")
		self.name = name
		self.house = house


	def __str__(self):
		return f"{self.name} is in {self.house}."

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		if not name:
			raise ValueError("Name is required.")
		self._name = name

	@property # getter
	def house(self):
		return self._house
	
	@house.setter # setter
	def house(self, house):
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is not valid.")
		self._house = house

	
def get_student():
	name = input("Name: ")
	house = input("House: ")
	return Student(name, house,)


def main():
	student = get_student()	# This function will return a Student class object
							# NtS: make sure a variable is eventually assigned to the class object
	student._house = "Number Four, Privet Drive"
	print(student)

main()
