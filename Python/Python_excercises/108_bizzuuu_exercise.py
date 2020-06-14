def check_if_div_3(num):
    return num % 3 == 0

def check_if_div_5(num):
    return num % 5 == 0

def fizz_buzz_print_check(num):
    if check_if_div_3(num) and check_if_div_5(num):
        print(f'{num}, is divisiable by both 3 and 5')

    elif check_if_div_5(num):
        print(f'{num}, is divisable by 5')

    elif check_if_div_3(num):
        print(f'{num}, is divisable by 3')

    else:
        print(f'{num}, is divisable by neither')

while True:
    num = input('div by 3 or 5 check: ')
    if 'exit' in num:
        print('broke the game')
        break


    if num.isnumeric():
        num = int(num)

    for number in range(1, num + 1):
        fizz_buzz_print_check(num)
        break





