# filipes code
def check_if_div3(num):
    return num % 3 == 0
    # if num % 3 == 0:
    #     return True
    # else:
    #     return False

def check_if_div5(num):
    return num % 5 == 0
    # if num % 5 == 0:
    #     return True
    # else:
    #     return False

def check_num(num1,num2):
    return num1 % num2 == 0
# Test 1: 3 div 3
# run the function with arguments 3,3
# if true returns true

# Test 2: 4 div 3?
# Run the function with arguments, 4, 3
# If true returns True
# If false returns False
# Expected Outcome: False

# Test 3: 5 div 5?
# Run the function with arguments, 5, 5
# If true returns True
# If false returns False
# Expected Outcome: True

# Test 4: 6 div 5?
# Run the function with arguments, 6, 5
# If true returns True
# If false returns False
# Expected Outcome: False

# Test 5: 15 div 3?
# Run the function with arguments, 15, 3
# If true returns True
# If false returns False
# Expected Outcome: True

# Test 6: 15 div 5?
# Run the function with arguments, 15, 5
# If true returns True
# If false returns False
# Expected Outcome: True

def fizz_buzz_print_check(num):
    if check_if_div5(num) and check_if_div3(num):
        print('it is divisible by 3 and 5')
    elif check_if_div5(num):  # only runs if the above if / elif stamentes were false
        print('yo it is div by 5')
    elif check_if_div3(num):
        print('yo it is div by 3')
    else:
        print(num)



while True:
    num = input('please give us a number to check if div by 3, 5 or 3 and 5?')
    if 'exit' in num:
        print('the force is with you...')
        break

    if num.isnumeric():
        num = int(num)

    for number in range(1, num + 1):
        fizz_buzz_print_check(number)






def check_if_digit_div_num(digit, num_div):
    if digit % num_div == 0:
        return True
    else:
        return False

def bizzbuzz(num1, num2, number):
    for digit in range(1, (int(number) + 1)):
        if check_if_digit_div_num(digit, num1) and check_if_digit_div_num(digit, num2):
            print('bizzzzuu')
        elif check_if_digit_div_num(digit, num2):
            print('zzuu')
        elif check_if_digit_div_num(digit, num1):
            print('bizz')
        else:
            print(digit)



