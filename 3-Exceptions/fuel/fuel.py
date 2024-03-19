def get_fuel():
    numer, decim = input("Enter the number of liters of fuel: ").split("/")
    try:
        return int(numer), int(decim)
    except ValueError:
        print("You must enter a number!")
        return None, None

while True:
    numer, decim = get_fuel()
    if numer is None or decim is None:
        break
    try:
        percentage_full = (numer / decim) * 100
        if percentage_full >= 100:
            print("F")
        elif percentage_full <= 0:
            print("E")
        else:
            print(f"{percentage_full:.0f}%")
        break
    except ZeroDivisionError:
        print("You can't divide by zero!")