students = [
	{"name": "Hermione", "house": "Gyffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gyffindor", "patronus": "Stag"},
	{"name": "Ron", "house": "Gyffindor", "patronus": "Jack Russell Terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
	print(student["name"], student["house"], student["patronus"], sep=": ")

# students = {
# 	"Hermione": "Gyffindor", 
# 	"Harry": "Gyffindor", 
# 	"Ron": "Gyffindor", 
# 	"Draco": "Slytherin"
# }

# for student in students:
# 	print(student, students[student], sep=": ")

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gyffindor", "Gyffindor", "Gyffindor", "Slytherin"]

# for i in range(len(students)):
# 	print(i+1, students[i])

# for student in students:
#     print(student)

# print(students[0])
# print(students[1])
# print(students[2])