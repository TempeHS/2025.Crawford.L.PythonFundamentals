# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f"Hello {name}!")

# name = input("What is your name? ")

# with open("names.txt", "a") as file:
#     file.write(name + "\n")

# print(f"'{name}' written to file.")

# names = []

# with open("names.txt", "r") as file:
#     for line in sorted(file):
#         names.append(line.rstrip())
		
# for name in names:
#     print(f"Hello {name}!")

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}.")


# import csv
# students = []
# with open("names.csv") as file:
# 	reader = csv.DictReader(file)
# 	for row in reader: # for row in reader:
# 		students.append({'name': row['name'], 'home': row['home'], 'house': row['house']})
# for student in sorted(students, key=lambda student: student['name']):
# 	print(f"{student['name']} is from {student['home']} and in house {student['house']}.")

import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=['name', 'home'])
	writer.writerow({'name': name, 'home': home})