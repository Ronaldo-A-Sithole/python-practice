#Variables
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
xp = 60
verified = True
print("Name:", name)
print("User ID:", user_id)
print("Progress:", progress)
print("XP:", xp)
print("Verified:", verified)

#Data types
#string
name = 'Erlich Bachman'      # have to use single or double quotes to indicate that it is a string
#integer
user_id = 16180339887        # have to use a whole number to indicate that it is an integer
#float
progress = 0.75              # Have to use a decimal point to indicate that it is a float
#boolean
verified = True              # In numbers boolean, True = 1, False = 0


#Multiple variables
name, user_id, progress, xp, verified = 'Erlich Bachman', 16180339887, 0.75, 60, True
print("Name:", name)
print("User ID:", user_id)
print("Progress:", progress)
print("XP:", xp)
print("Verified:", verified)

#Unpacking
data = ['Erlich Bachman', 16180339887, 0.75, 60, True]
name, user_id, progress, xp, verified = data
print("Name:", name)
print("User ID:", user_id)
print("Progress:", progress)
print("XP:", xp)
print("Verified:", verified)