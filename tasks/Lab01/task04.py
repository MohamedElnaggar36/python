# 4. Write a program that remove all vowels from the input word and generate a brief version of it.
newString = input("enter string: ")
vowels = "aeiou"
for chars in vowels:
    newString = newString.replace(chars, "")
print(newString)