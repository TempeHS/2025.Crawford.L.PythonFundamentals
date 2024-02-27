def main():
    number = get_number
    meow(number)
    
def get_number():
    while True:
        n = int(input("Number of 'Meows'? "))
        if n > 0:
            return n
    
def meow(n):
    for _ in range(n):
        print("Meow")

main()

# while True:
#     n = int(input("Number of 'Meows'? "))
#     if n > 0:
#         break

# print("Meow\n" * n, end="")

# for _ in range(3):
#     print("Meow")

# i = 0 
# rep = int(input("Enter a number: ")) # 3
# while i < rep:
#     print("Meow")
#     i += 1

# print("Meow")
# print("Meow")
# print("Meow")