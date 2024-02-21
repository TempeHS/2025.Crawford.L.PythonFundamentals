name = input("What is your name? ").strip().title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# if name == "Harry" or "Hermione" or "Ron":
#     print("Gryffindor")
# # elif name == "Hermione":
# #     print("Gryffindor")
# # elif name == "Ron":
# #     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")