#Tuples cannot be changed, they are immutable. They are defined using parentheses ().
t = (1, 2, 3, 4, 5)
print(t)  # Output: (1, 2, 3, 4, 5)
print(t[0])  # Output: 1
print(t[-1])  # Output: 5
print(t[1:4])  # Output: (2, 3, 4)

""""To change a tuple, you can convert it to a list,
 make the changes, and then convert it back to a tuple."""
#example
t_list = list(t)
t_list[0] = 10
t = tuple(t_list)
print(t)  # Output: (10, 2, 3, 4, 5)

#Dictionaries are defined using curly braces {} and consist of key-value pairs.
my_dict = {"name": "John", "age": 30, "city": " New York"}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': ' New York'}
#Accessing values in a dictionary   
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30

#looping through a dictionary
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 30, city New York  

print(key +":" + str(my_dict[key]))  # Output: city: New York
