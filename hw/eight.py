"""Задача 1: Индексация и Срезы
Создайте переменную sentence со значением "Привет мир! Меня зовут Python."
Выведите первый и последний символы строки, используя индексацию.
Выведите подстроку, включающую слово "мир", используя срез.
Разверните строку, используя срез.
Выведите каждый второй символ строки."""
# sentence = "Привет мир! Меня зовут Python."
# print(sentence[0])
# print(sentence[-1])
# print((sentence[ 7:10:].split()))
# print(sentence[::-1])
# print(sentence[::2])




"""Задача 2: Конкатенация строк
Примите от пользователя first_name и last_name и присвойте им ваше имя и фамилию.
Сконкатенируйте эти строки, чтобы получить полное имя.
Создайте строку greeting с приветствием и используйте конкатенацию, чтобы добавить полное имя.
Добавьте пробел между именем и фамилией, используя конкатенацию.
Создайте строку age с вашим возрастом и конкатенируйте её с предыдущими данными."""
# first_name = input("Имя ")
# last_name = input("Фамилия ")
# age_name = input("Возраст ")
# name = first_name +" "+ last_name
# greeting = print("Добрый день"+" "+ name + " " + age_name)

"""Задача 3: Методы строк
Создайте строку text со значением "Программирование на Python - это увлекательно!".
Используйте встроенный метод , чтобы заменить слово "Python" на "JavaScript".
Уберите пробелы в начале и конце строки, используя встроенный метод .
Проверьте, состоит ли строка только из букв.
Выведите индекс первого вхождения буквы "а" в строке."""

# text = "Программирование на Python - это увлекательно!    "
# print((text.replace("Python", "Javascript")).strip().isalpha())
# print(text.find("а"))   




"""Задача 4: Форматирование строк
Запросите у пользователя ввод имени и фамилии. Выведите приветствие, используя форматирование %.
Снова запросите у пользователя ввод имени и фамилии. Выведите приветствие, используя метод .format.
Попросите пользователя ввести имя и фамилию. Выведите приветствие с использованием f-строки."""

# name , surname = input("Имя: "),input("Фамилия: ")
# welcome = print('Hello mr/mrs %s %s ' %(name , surname))

# print('Welcome mr/mrs {} {} ' .format(name , surname))
# print(f'Welcome mr/mrs {name} {surname}')




"""Задача 5: Дополнительные методы
Создайте строку sentence со значением "Строки - это базовый тип данных в Python.".
Подсчитайте сколько раз слово "Python" встречается в строке.
Разделить строку на слова и сохраните результат в списке.
Снова используйте созданный список слов и объедините слова обратно в строку, разделяя их запятой.
Примените метод swapcase к строке и выведите результат"""

# sentence = "Строки - это базовый тип данных в Python."
# print(sentence.count("Python"))
# sentence_ls = sentence.split(" ")
# sentence_ls = ",".join(sentence_ls)

# print(sentence_ls.swapcase())





