# SIMPLEST - Restaurant Waiter Helper
menu = ['pizza','burger','mixed grill','ramen']
food_order = []
# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
print('Here is the menu today')
for items in menu:
    print(items.capitalize())


#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
while True:
    order_item = input("\nWhat would you like to order? Say 'When' when complete.  ")

    if order_item != "When":
        food_order.append(order_item)
    else:
        print("\nYour order:\n")
        for i in food_order:
            print(i.capitalize())
        break

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD --- Not necessary - can be done as an extra. Go search what DOD means in scrum
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []


# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything