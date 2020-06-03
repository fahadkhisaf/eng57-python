# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
import random
magic_number = random.randrange(1, 201)

# I need to ask user for input
user_input = int(input('What is the magic number? '))
if user_input == magic_number:
    print('hoorayyyy!!!')
else:
    print('thats incorrect ')

print(magic_number)
# I need to check if this input matches a magic_number


# I need to let the user know if the response was right or not
#self five