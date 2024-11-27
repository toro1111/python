s = input("Enter a word: ")
c = s[0]
str1 = s[1:].replace(c, '$')
print(c + str1)
