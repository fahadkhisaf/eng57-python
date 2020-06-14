# Define the following variables
# name, last_name, age, eye_color, hair_color
# name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these
name = input('What is your name? ')
age = int(input('How old are you? '))
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print(f'Hello {name}! Welcome, your age is {age}')

#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'
dob = int(input('What year where you born in? '))
year = 2020
print(f'You are {year - dob} years old')
#Extra - Cast your input
# full_name = input("What is your full name? ")
# print(full_name)
# print("Beautiful name,", full_name)
# age = int(input("How old are you? "))



