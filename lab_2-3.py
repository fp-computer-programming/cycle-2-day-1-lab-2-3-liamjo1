# Create a Python file named lab_2-3.py

# Set a equal to 2. Using the type() function, print the type of variable a

# Change the type of a to a float using a = float(a). What is the result of printing type(a) now?

# Convert a to a string. Check its type with a print statement. What has changed?

# Convert a to a Boolean. Print the result of a == 2. What is the result? Why? (Answer as a comment)


a = 2
print(type(a))

a = float(a)
print(type(a))
# type has changed to 'class float'

a = str('a')
print(type(a))
# type has changed to 'class str'

a = bool(a)
a == 2
print(a)
#result is true because a is a boolean and a does eqaul 2

