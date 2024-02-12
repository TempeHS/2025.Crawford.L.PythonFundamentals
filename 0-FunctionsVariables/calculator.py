'''
x = float(input("Enter x: "))  # Ask the user for x
y = float(input("Enter y: "))  # Ask the user for y

z = x / y

print(f"{z:.2f}") # Print the result
'''

def main():
    x = float(input("What is x? "))
    print("x squared is", square(x))
    
def square(n):
    n = n**2
    return n

main()