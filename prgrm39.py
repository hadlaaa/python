def add(*args):
    """function to add variable length arguments"""
    total = 0
    for n in args:
        total = total + n
    return total

numbers = input("Enter integers separated by space: ").split()
numbers = list(map(int, numbers))

print("Sum =", add(*numbers))
