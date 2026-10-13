# (a) Generate positive list of numbers

numbers = [-5, 2, -3, 4, 6, -1]
positive = [n for n in numbers if n > 0]
print("Positive numbers:", positive)


# (b) Square of N numbers

n = int(input("Enter N: "))
squares = [i * i for i in range(1, n + 1)]
print("Squares:", squares)


# (c) Form a list of vowels selected from a given word

word = input("Enter a word: ")
vowels = [ch for ch in word if ch in "aeiouAEIOU"]
print("Vowels:", vowels)


# (d) Form a list of ordinal values of each element of a word

word = input("Enter a word: ")
values = [ord(ch) for ch in word]
print("Ordinal values:", values)
