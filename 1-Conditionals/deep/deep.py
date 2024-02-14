def main(inp):
    if inp.strip() == 42:
        print("Yes")
    elif inp.strip().title() == "Forty Two":
        print("Yes")
    elif inp.strip().casefold() == "forty-two":
        print("Yes")
    else:
        print("No")
        
main(
    input("What is the meaning of life? ")
)