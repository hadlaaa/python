list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

# (a) Same length
if len(list1) == len(list2):
    print("(a) Lists are of the same length")
else:
    print("(a) Lists are not of the same length")

# (b) Same sum
if sum(list1) == sum(list2):
    print("(b) Lists sum to the same value")
else:
    print("(b) Lists do not sum to the same value")

# (c) Any common value
if set(list1).intersection(set(list2)):
    print("(c) Both lists contain common value(s)")
else:
    print("(c) No common values")
