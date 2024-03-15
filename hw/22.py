
    # Задача 1: Валидация пароля

    # Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:
password = input("Введите пароль: ")
min_length = 8
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special_char = any(char in "!@#$%^&*()_-+=<>?/" for char in password)
if len(password) < min_length:
        print("Длина пароля должна быть не менее 8 символов.")
elif not has_uppercase:
        print("Пароль должен содержать хотя бы одну заглавную букву (A-Z).")
elif not has_lowercase:
        print("Пароль должен содержать хотя бы одну строчную букву (a-z).")
elif not has_digit:
        print("Пароль должен содержать хотя бы одну цифру (0-9).")
elif not has_special_char:
        print("Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/")
else:
    print("Пароль принят.")
print(password)




    #     Длина пароля должна быть не менее 8 символов.
    #     Пароль должен содержать хотя бы одну заглавную букву (A-Z).
    #     Пароль должен содержать хотя бы одну строчную букву (a-z).
    #     Пароль должен содержать хотя бы одну цифру (0-9).
    #     Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/

    # Напишите программу, которая запрашивает у пользователя пароль и затем проверяет, удовлетворяет ли он всем критериям. Если пароль удовлетворяет всем критериям, программа должна сообщить, что пароль принят. В противном случае, программа должна вывести сообщение об ошибке, указывая, какие критерии не выполняются.

# Задача 2: Обработка ошибок при работе с элементами списка:

# Создайте список чисел и попробуйте выполнить некоторые операции над элементами списка. Обработайте исключения, такие как IndexError, ValueError и ZeroDivisionError.
# ls = [1,2,3,4,5,6,7]
# try:
#     add_ls = input("Добавить в список: ")
#     ls.append(add_ls)
#     print(ls[3])
#     divide = ls[6] / ls[1]
#     print(divide)
# except (IndexError, ValueError ,ZeroDivisionError) as e:
#     print(e)


# Задача 3: Поиск значения в словаре с обработкой исключения:

# Создайте словарь с данными (например, словарь с именами и возрастами людей). Затем запросите у пользователя имя и попробуйте найти возраст этой персоны в словаре. Обработайте исключение, если имя не найдено.
# dict_ = {
#     'Alex':18,
#     'Moana': 25,
#     'Andrew' : 48,
#     'Tima' : 21,
# }
# try:
#     user = input('Write name: ')
#     if user in dict_:
#         print(dict_[user])
#     else:
#         raise KeyError
# except KeyError:
#     print("Имя не найдено!")