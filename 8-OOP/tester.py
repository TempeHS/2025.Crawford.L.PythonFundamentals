class Student:
	def __init__(self, name, house, patronus):
		# self.name = name
		# self.house = house
		if not name:
			raise ValueError("Name is required.")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is not valid.")
		self.name = name
		self.house = house
		self.patronus = patronus
	def __str__(self):
		return f"{self.name} is in {self.house}."

	
def get_student():
	name = input("Name: ")
	house = input("House: ")
	patronus = input("Patronus: ")
	return Student(name, house, patronus)


def main():
	student = get_student()
	print(student)
 
main()