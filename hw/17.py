# # dаны 2 списка:

# list_a = [1, 2, 39, 5, -6, 7, 8.1, 9, 10, -43, -134, 3.14, 2.55, 
# "Lenovo", "Acer", "Asus"]

# list_b  = [123, -1.85, 43, -4.4, 8.16, - 5, 3.26, 21, 22, -43.97,
#  "Dell", "HP", "Lenovo", "Acer" ]

# # Создать новые списки и вывести их результаты:

# #     Где будут только целые числа, которые больше 4
# sort_four_list = [x for x in list_a + list_b if isinstance(x,int) and x > 4]
# #     Где будут только числа с плавающей точкой, имеющие отрицательное значение
# sort_float_list = [x for x in list_a + list_b if isinstance(x,float) and x < 0]
# #     Где будут только наименования производителей ноутбуков
# sort_words_list = [x for x in list_a + list_b if isinstance(x,str)]


# # Продолжить работу со списками, содержащие цифры и вывести их результат:

# #      Вставить в середину каждого списка новое значение(любое)
# center_list_four = len(sort_four_list) // 2
# sort_four_list.insert(center_list_four, 55)
# center_list_float = len(sort_float_list) // 2
# sort_float_list.insert(center_list_float, 1.25)
# center_list_word = len(sort_words_list) // 2
# sort_words_list.insert(center_list_float, 'dsdds')

# #     Найти сумму элементов в каждом списке
# print(sum(sort_four_list))
# print(sum(sort_float_list))

# #     Посчитать количество элементов в каждом списке

# print(len(sort_four_list))
# print(len(sort_float_list))
# print(len(sort_words_list))

# # В списках с наименованиями (вывести результат):

# #     Проверить наличие повторяющихся данных, если есть удалить.
# fsdjnfdsjnvf = list(set(sort_words_list))
# fsdjnfdsjnvf.insert(0,"BMW")
# fsdjnfdsjnvf.append("lexus")
# print(fsdjnfdsjnvf)

#     Добавить в начало и конец по одному производителю.

 

# Задание 2 (20 баллов)

# Напишите программу имитирует регистрацию пользователя.

# Программа должна запросить у Вас:

# Name

# Email

# # Password
# user_name = input("Name: ")
# user_email = input("Email: ")
# user_password = input("password: ")
# Программа должна вывести сообщение:
# <name>, Вы успешно зарегистрировались, информация отправлена на <Email>


# Используйте разные методы форматирования сторок (5 методов) и напишите в комментариях 
# какой метод вам больше всего понравился и почему.

# # Продолжение задание №2 (20 баллов)

# #  Ваша программа должна проверить:

# #     введенное имя на наличие в конце хотя бы одной цифры
# #     введенный пароль на наличие только чисел
# #     введенный email на окончание символами ".kg" 
# #     в случае ошибки выдавать соответствуещее сообщение
# print(isinstance(user_name,float))
# print(isinstance(user_password,int))
# if ".kg" in user_email[-3:]:
#     print("True")
# else:
#     print("False")

# print(f"{user_name} Вы успешно зарегистрировались, информация отправлена на {user_email}")
# fsdklfgmdsl = "%s Вы успешно зарегистрировались, информация отправлена на %s" % (user_name,user_email)
# print(fsdklfgmdsl)
# print("{} Вы успешно зарегистрировались, информация отправлена на {}".format(user_name,user_email))
 

# Задание №3 (20 баллов)

# Напишите программу, которое учитывает количество уникальных букв в слове. Уникальные буквы — это те, которые встречаются всего один раз.

counter_bukvy = {}
user_string = input("Vvedite slovo: ")
for bukva in user_string:
    if bukva in counter_bukvy:
        counter_bukvy[bukva] += 1
    else:
        counter_bukvy[bukva] = 1
unique_count = sum(1 for count in counter_bukvy.values() if count == 1)
print(unique_count)
# Пример 1:

# Введите слово: привет
# Кол-во уникальных букв: 6

# Пример 2:

# Введите слово: лава
# Кол-во уникальных букв: 2

# Задание №4 (10 баллов)

# # Асан слишком ленивый чтобы считать длину окружности и решил написать программу которая будет считать вместо него длину, помогите написать ему программу, которая спрашивает у Асана радиус окружности и выдает (округленный до верхнего значения ответ, если радиус окружности больше или равен 10) ответ (использовать библиотеку math)
# import math
# radius = float(input("Введите радиус окружности: "))
# circumference = 2 * math.pi * radius
# if radius >= 10:
#     circumference = (circumference // 1) + 1
# print(f"Длина окружности: {circumference}")