# Операторы сравнения
# условные операторы
# логические операторы


# ------------------------------------------
# Опеораторы сравнения
# <,>,==(равно),!=(не равно), <=,>=

# 1 < 5 --> False
# 7 < 9 --> True

# print('ABC12323212' > 'abc123')

# 1 2 4 8 16 32 64 128 256 512 1024 2048
# 0 0 1 1 0  1
# 44 ---> 101100

# a = 'A'
# num = 123
# print(ord(a))
# print(chr(num))

# Условные операторы
# if
# elif
# else

# if <condition>:  
    # <body if> срабатывает если в condition if придет True
# [elif] <condition>
    # <<<<<<<<<<<<<<<<<,body elif>
# [else]:
    # <body else> сработает если во всех выше стоящих условияъ пришло false

# string = input('ENter smt:').lower()

# if string == 'hello':
#     print('hi niga')
# elif string == 'john':
#     print('welcome my brother')
# elif string == 'abra':
#     print('sdsd')
# else:
#     print('boje ustal')

# print('Registrator Form:')
# email = input('Enter your email: ')
# password = input('Enter the password: ')
# password2 = input('Enter password confimation: ')
# if len(password) < 8:
#     raise ValueError('Too short! At least 8 symbol')
# elif password.isdigit():
#     raise ValueError('Invalid PAssword! Oly digits!')
# elif password.isalpha():
#     raise ValueError('Invalid Password! Only alphabet!')
# password2 = input('ENter password confimation: ')

# if password != password2:
#     raise ValueError('Passwords didnt\'t math!')
# index = email.find('@')
# print(f'Succefully registered! Hello Mr/Nrs {email[:index]} !') 


age = input('Enter your age: ')

if age.isdigit():
    age = int(age)
else:
    raise Exception('Invalid value for age')


if age < 18:
    print(f'Access Denied! Come again after {18 - age} year')

else: 
    print('you can buy it!')



money = 1_000_001
status = 'premium'

if money > 1_000_000 and status == 'premium':
    print('You\'re president of our club!')
elif money > 1000000 or status == 'premium':
    print('You\'re minister of our club')
else:
    print('you\'re ho')
