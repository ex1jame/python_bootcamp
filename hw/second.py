# # """""
# # 1) Напишите программу, которая генерирует
# #  случайное число (целое или дробное) от 1 до 100,
# # а затем предлагает пользователю угадать это число. 
# # Программа должна предоставить подсказки о том, больше или меньше введенное число загаданного.
# # import random
# # a = round(random.uniform(1, 100),1 )     #, random.randint(1, 100)
# # print(a)
# # i = 0
# # while i < 3:
# #     guess = float(input("Guess the number: "))
# #     if guess == a:
# #         print("A lovko ty eto pridumal")
# #         i = 3
# #     elif guess > a:
# #         print("Ваше число меньше, чем задумал компьютер")
# #     elif guess < a:
# #         print("Ваше число больше, чем задумал компьютер")
# #     i += 1


# # 2)Напишите программу, которая преобразует температуру из градусов Цельсия в градусы Фаренгейта и наоборот. Позвольте пользователю выбирать тип преобразования.
# # 
# # _

# # while True:
# #     guess = int(input("Выберите что вы хотите преобразовать 1 цельсий, 2 фаренгейт или остановить программу: "))
# #     if guess == 1:
# #         cel = float(input("Температуру цельсия: "))
# #         f1 = 1.8 * cel + 32
# #         print(f"Температура Фаренгейта равна {f1}")
        
# #     elif guess == 2:
# #         f = float(input("Температуру фаренгейта: "))
# #         cels = (f - 32) / 1.8
# #         print(f"Температура Фаренгейта равна {cels}")
# #     elif guess == 3:
# #         print("Thx the using program sps")
# #         break    
    



# # """""
# # 3) Реализуйте программу, которая рассчитывает ежемесячные выплаты по ипотеке. Пользователь должен ввести сумму кредита, годовую процентную ставку и срок кредита. 
# # '''''
# # sum_credit = input("Введите сумму кредита: ")  
# # year_per = input("Введите годовую процентную ставку: ")  
# # times_credit = input("Введите срок кредита: ")
# # sum_credit = int(sum_credit)
# # year_per = int(year_per)
# # times_credit = int(times_credit)
# # monthly_times_credit = (year_per / 100 ) / 12
# # total_credit = times_credit * 12
# # monthly_payment = (sum_credit * monthly_times_credit) / (1 - (1 + monthly_times_credit) ** -total_credit)
# # print("Ежемесячный выплаты: ", monthly_payment)

# # """""
# # 4) Напишите программу, которая генерирует первые n чисел в последовательности Фибоначчи, где n вводится пользователем.
# # """""
# fib1 = 0
# fib2 = 1
 
# n = int(input())
 
# print(fib1, fib2, end=' ')
 
# for i in range(1, n+1):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# # """""
# # 5) Попросите пользователя ввести количество часов, а затем выведите эквивалентное количество минут.
# # '''''
# # guess = int(input("Введите количество часов: "))
# # print(guess * 60 )
# # """""
# # 6) Запросите у пользователя цену товара и количество единиц товара, а затем выведите общую стоимость.
# # '''''
# # cost_goods = int(input("Введите цену товара: "))
# # val_goods = int(input("Введите количество единиц товара: "))
# # print("Общая стоимость: ",cost_goods * val_goods)

# # ““”
# # 7) Количество дней в годах: Введите возраст пользователя и выведите, сколько дней он прожил (учитывая невисокосные года).
# # '''''
# # guess = int(input("Введите возраст: "))
# # guess_sum = guess * 365
# # print("Вы прожили",guess_sum,"дней")

# # """""
# # 8) Попросите пользователя ввести количество дней, а затем выведите, сколько это недель и сколько дней осталось.
# # '''''
# # guess = int(input("Введите количество дней: "))
# # guess_weaks = guess // 7
# # day = guess % 7
 

# # print("Недели: ",guess_weaks,"Дни: ", day)
# # """""
# # 9) Extra. Создайте игру "Камень-ножницы-бумага" с компьютером. 
# # Пользователь вводит свой выбор, а программа генерирует случайный выбор компьютера.
# # '''''
# # import random
# # guess = input("Введите свой выбор: ")
# # random_list = ("Камень","Ножницы","Бумага")
# # random_try = random.choice(random_list)
# # print("Вы выбрали ", guess,"!")
# # print("Компьютер выбрал ", random_try,"!")
# # if random_try == guess:
# #     print("Ничья")
# # elif guess == "Камень":
# #     if random_try == "бумага":
# #         print("Камень бьет бумагу! Вы проиграли!")
# #     else:
# #         print("Камень бьет ножницы! Вы победили!")
# # elif guess == "Бумага":
# #     if random_try == "ножницы":
# #         print("Бумага бьет ножницы! Вы проиграли!")
# #     else:
# #         print("бумага бьет камень! Вы победи!")
# # elif guess == "Ножницы":
# #     if random_try == "камень":
# #         print("Ножницы бьет камень! Вы проиграли!")
# #     else:
# #         print("Ножницы бьет бумага! Вы проиграли !")