# list comprehensions - генераторы списков
# list comprehensions - упрощенный подход к создание списков,который задействует в себе
# цикл for,а так же конструкцию if для определения того,что в итоге попадает в наш список

#list -> 0 - 200 -> четные

# ls = []
# for i in range(0,201):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# ls = list(range(0,201,2))
# print(ls)

# ls =[x for x in range(0,201,2)]
# ls =[x for x in range(0,201)if x % 2 == 0]

# print(ls)

# list: 0 - 300,delyatsa na 3 i na 2

# ls = []
# for x in range(0,301):
#     if x % 2 ==0 and x % 3 == 0:
#         ls.append(x)


# print(x)

# ls = [x for x in range(0, 301) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# list: 0 - 100 -> x % 2 == 0 : x ** 2,x % 3 == 0: x ** 3


# ls = []
# for x in range(0,101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     if x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)


# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0,101) if x % 2 == 0 or x % 3 == 0]
# print(ls)


# -------------------------------------------
# newlist = [expression for item in iterable <if condition == True>]

# ls = [str(i ** 2) for i in range(0,11)]
# print(ls)\
ls = [[1,2,3],[4,5,6],[7,8,9]]
td = []
# for x in ls:
#     td += x
# print(td)
# for x in ls:
#     for num in x:
#         td.append(num)
# print(td)
# res = [num for x in ls for num in x]
# print(res)
# -----------------------------

# from datetime import datetime
# start = datetime.now() #11.41.35
# ls = []
# for x in range(0, 100_000):
#     ls.append(x)
# finish = datetime.now() #11.41.46
# print(finish-start)