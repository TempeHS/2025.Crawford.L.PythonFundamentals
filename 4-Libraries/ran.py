import sys
if len(sys.argv) > 2:
    print("Too many arguments.")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("You have not entered your name as an argument.")
    sys.exit(1)
else: 
    print(f"Hello, your name is {sys.argv[1]}!", end=" ")
    print(f"You have ran the file '{sys.argv[0]}'.")
# except IndexError:
#     print("You have not entered your name as an argument.")
    