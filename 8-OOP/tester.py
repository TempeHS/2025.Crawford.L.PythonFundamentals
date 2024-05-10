class Student:
	def __init__(self, name, house, patronus):
		# self.name = name
		# self.house = house
		# if not name:
		# 	raise ValueError("Name is required.")
		self.name = name
		self.house = house
		self.patronus = patronus

	def __str__(self):
		return f"{self.name} is in {self.house}."

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
	patronus = input("Patronus: ")
	return Student(name, house, patronus)


def main():
	student = get_student()	# This function will return a Student class object
							# NtS: make sure a variable is eventually assigned to the class object
	print(student)

main()

print("End of tester.py")

