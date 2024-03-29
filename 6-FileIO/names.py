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

students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {'name': name, 'house': house}
        # student['name'] = name
        # student['house'] = house
        students.append(student)
        
def get_name(student):
    return student['name']

def get_house(student):
    return student['house']

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}.")