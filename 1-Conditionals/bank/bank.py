def main(greet):
    notReq = "hello"
    if greet.strip().casefold() == "hello":
        # $0
        print("$0 (A)")
    elif notReq in greet.strip().casefold():
        # $0
        print("$0 (B)")
        '''
        I had to place the previous code because I don't know how to chain boolean operators in a single if statement.
        '''
    elif greet.strip().casefold().startswith("h"): # If the greeting starts with "h"
        # $20
        print("$20")
    else:
        # $100
        print("$100")

main(
    input("How do you greet people? ") # Asks the user for input
)

# 