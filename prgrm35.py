def interest(p, t, senior):
    if senior == "yes":
        r = 12
    else:
        r = 10
    return (p * t * r) / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
senior = input("Senior citizen (yes/no): ")

print("Simple interest =", interest(p, t, senior))
