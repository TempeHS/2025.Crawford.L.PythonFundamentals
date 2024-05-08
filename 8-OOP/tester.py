class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house
	def who_from(self):
		return f"{self.name} from {self.house}"
	

name = input("Name: ")
house = input("House: ")
student = Student(name, house)


print(
	student.who_from()
)	