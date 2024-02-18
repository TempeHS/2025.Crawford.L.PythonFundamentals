op = input("Operation: ")
x, y, z = op.split(" ")


if y == "+":
    out = (float(x) + float(z))
elif y == "-":
    out = (float(x) - float(z))
elif y == "*":
    out = (float(x) * float(z))
else:
    out = (float(x) / float(z))
print(round(out, 1))