def main():
    x = int(input("Insert a number: "))

    if is_even(x):
        print("The number is even.")
    else:
        print("The number is odd.")
        
def is_even(n):
    return n % 2 == 0

# x = int(input("Insert a number: "))

# if x % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

main()