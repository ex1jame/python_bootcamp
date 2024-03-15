# Задание 1

# Вы решили сделать проверку при входе, и пускать на сайт только «своих» ребят.
#  Для этого Вам необходимо составить список никнеймов, которые будут иметь доступ.

# Необходимо, что при запуске кода, программа запрашивала никнейм, и 
# либо пускать на сайт (выведется сообщение «Ты – свой. Приветствую, 
# любезный {НИК_ПОСЕТИТЕЛЯ}!»), либо нет (в этом случае будет такой текст: 
# «Тут ничего нет. Еще есть вопросы?»).

# Используйте цикл While, для того чтобы программа вновь и вновь запрашивала 
# никнейм пользователя, до тех по пока не ввести «правильный» никнейм.

# roles = {
#     1: 'Tirion',
#     2: 'Olymp',
# }


# while True:
#     guess = input("Введите свое имя: ")
#     if guess == roles[1]:
#         print(f"Ты – свой. Приветствую,любезный {guess}!")
        # break
#     else:
#         print("Тут ничего нет. Еще есть вопросы?")

# Задание 2

 

# Создать программу имитирующий чат:

# Чат должен работать со следующими фразами:

# "Кто ты?" -  "Я программа"

# "Что делаешь?" - "Работаю"

# "Как дела” - "Хорошо"

# "Как это работает?” - "Как-то так"

# "Где ты?” - "У тебя на компе"
# commands_bot = {
#     "Кто ты?":"Я программа",

#     "Что делаешь?":"Работаю",

#     "Как дела":"Хорошо",

#     "Как это работает?":"Как-то так"
# }

# Написать чат-бота, который будет ждать от пользователя ввод вопроса из 
# вышеописанных фраз и давать на него соответствующий ответ. 
#  Ввод данных будет осуществляться вечно, до тех пор, пока пользователь не введет букву "q". 
# Сообщить, если введен вопрос, которого нет в списке.

# while True:
#     words = input("napawi command: ")
#     if words == 'q':
#         print("End")
#         break
#     if words in commands_bot:
#         print(commands_bot[words])
#     else:
#         print("I dont understand this")
        

    

        






# Задание3

# Напишите программу, которая будет суммировать все числа, 
# введенные пользователем, игнорируя при этом нечисловой ввод. 
# Выводите на экран текущую сумму чисел после каждого очередного ввода.
# Ввод пользователем значения, не являющегося числовым, должен приводить к 
# появлению соответствующего предупреждения, после чего пользователю должно
# быть предложено ввести следующее число. Выход из программы будет осуществляться 
# путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает 
# целочисленные значения и числа с плавающей запятой.
# sums = 0
# while True:
#     guess = input('Введите числа для суммирования: ')
#     numbers = guess.split()
#     if not guess:
#         break
#     for i in numbers:
#         try:
#             number = float(i)
#             sums += number
#             print("Текущая сумма: ",sums)
#         except ValueError:
#             print("Ошибка!Введите корректные числа: ")
# print("Итоговая сумма", sums)

# import re


# input_string = 'dsad454.4542dxc5..7.2.6'
# numbers = re.findall(r'\d+\.\d+|\d+', input_string)
# b                                                                                                                        
# # Преобразуем строки в числа и выводим результат
# numbers = [float(num) for num in numbers]
# print(numbers)
import random

def generate_lotto_numbers():
    return list(range(1, 76))

def shuffle_lotto_numbers(numbers):
    random.shuffle(numbers)

def simulate_lotto_game():
    card_numbers = generate_lotto_numbers()
    shuffle_lotto_numbers(card_numbers)

    winning_numbers = set(random.sample(card_numbers, 5))
    extracted_numbers = set()

    turns = 0
    while not extracted_numbers.issuperset(winning_numbers):
        extracted_numbers.add(card_numbers.pop(0))
        turns += 1

    return turns

def main():
    simulations = 1000
    total_turns = 0
    min_turns = float('inf')
    max_turns = 0

    for _ in range(simulations):
        turns = simulate_lotto_game()
        total_turns += turns
        min_turns = min(min_turns, turns)
        max_turns = max(max_turns, turns)

    average_turns = total_turns / simulations

    print(f"Минимальное количество ходов: {min_turns}")
    print(f"Максимальное количество ходов: {max_turns}")
    print(f"Среднее количество ходов: {average_turns}")

if __name__ == "__main__":
    main()
