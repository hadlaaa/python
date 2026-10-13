word=input("enter words separated by space:").split()
longest_word=max(word,key=len)
print("longest word:",longest_word)
print("longest of the longest word:",len(longest_word))
