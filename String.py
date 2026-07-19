#Strings
x = "Hello, World!"
print(x)

#Quotes Inside Quotes
y = "He is called 'Johnny'"
z = 'She is called "Jane"'
print(y)
print(z)

#Multiline Strings
a = """This is a multiline string that spans
multiple lines."""
print(a)

#Strings are Arrays it means that you can access individual characters in a string using indexing.
b = "Hello, World!" 
print(b[0])  # This will print the first character of the string, which is 'H'.
print(b[7])  # This will print the eighth character of the string, which is 'W'.

#Looping Through a String it means that you can loop through each character in a string using a for loop.
for char in b:
    print(char)  # This will print each character in the string on a new line.

#String Length it means that you can find the length of a string using the len() function.
c = "Hello, World!"
print(len(c))  # This will print the length of the string, which is 13.

#Check String it means that you can check if a certain substring exists within a string using the in keyword.
d = "Hello, World!"
print("Hello" in d)  # This will print True because "Hello" is a substring of d.

if "World" in d:
    print("Yes, 'World' is present in the string.")  # This will print if 'World' is found in the string.

#String Format it means that you can format strings using the format() method.
age = 25
txt = "My name is John, and I am {}"
print(txt.format(age))


