
string = input("Enter a string: ")

if len(string) < 3:
    result = string
elif string.endswith("ing"):
    result = string + "ly"
else:
    result = string + "ing"

print("Result:", result)

