def main():
    height = int(input("Enter the height: "))
    pyramid(height)
    
def pyramid(n):
    for i in range(n):
        print("*" * (i + 1))

main()