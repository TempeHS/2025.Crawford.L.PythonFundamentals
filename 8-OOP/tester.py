class Student:
	def __init__(self, name, house):
		# self.name = name
		# self.house = house
		if not name:
			raise ValueError("Name is required.")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is not valid.")
		self.name = name
		self.house = house
	def __str__(self):
		return f"{self.name} is in {self.house}."

	
def get_student():
	name = input("Name: ")
	house = input("House: ")
	return Student(name, house)


def main():
	student = get_student()
	print(student)
 
main()