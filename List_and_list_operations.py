#lists
my_list = [1, 2, 3, 4, 5]
print(my_list)

print(my_list[0])  # Accessing the first element
print(my_list[2])  # Accessing the third element
print(my_list[4])  # Accessing the fifth element

#list operations
#adding elements to a list

#Append method
my_list.append(6)  # Adding an element at the end
print(my_list)  

#Insert method
my_list.insert(2, 10)  # Inserting an element at index 2
print(my_list) 

#Removing elements from a list
#Remove method  
my_list.remove(10)  # Removing the element with value 10
print(my_list)

#Pop method
my_list.pop(3)  # Removing the element at index 3
print(my_list)  

#Clearing the list
my_list.clear()  # Removing all elements from the list 

#reinitializing the list
my_list = [1, 2, 3, 4, 5]
print(my_list)

#reverse method
my_list.reverse()  # Reversing the list
print(my_list)

#sorting the list
my_list.sort()  # Sorting the list in ascending order
print(my_list) 

#length of the list
print(len(my_list))  # Getting the length of the list   

#Copying a list
#Copy method
new_list = my_list.copy()  # Creating a copy of the list
print(new_list)  # Printing the copied list

