def generate_full_name(first_name , last_name):
    return first_name + ' ' + last_name


def sum_two_num(num1,num2):
    return num1 + num2


def cube_of_num(num3):
    return num3**3


def square_of_num(num4):
    return num4**2


def pattern_print(num5):
    for i in range(1,num5):
        for j in range(1,i+1):
            print('*',end = ' ')
        print()

def good_morning_message():
    name = input('Enter persons name here :')
    message = 'Good Morning '
    good_message = message  +  name 
    return good_message
