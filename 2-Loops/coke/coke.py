required_amount = 50
input_amount = 0
while True:
    in_coin = int(input("Insert coin: ").strip())
    if in_coin in [5, 10, 25]:
        input_amount += in_coin
        required_amount -= in_coin
        print(f"You inserted a coin. Total input: {input_amount} cents.")
        if required_amount == 0:
            print("You have inserted enough money.")
            break
        elif required_amount < 0:
            print(f"Change owed: {abs(required_amount)}")
            break
        else:
            print(f"Amount due: {required_amount}")
    else:
        print(f"Invalid coin. Amount due: {required_amount}")
        continue