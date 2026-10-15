n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    num = int(input("Enter item: "))
    total += num

print("Sum =", total)
