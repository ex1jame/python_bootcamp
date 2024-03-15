# ОБЛАСТИ ВИДИМОСТИ И ПРОСТРАНство имен (scopes)
# технологии которая опеределяет контекст имени,в рамках которого мы можем ее использовать

# a = 5

# def func(b):
#     print(a)
    
# func(2)

# # built-ins(встроенная область видимости) - print(), len()
# # global(глобальная) - область одного файла
# # <enclosed>(замкнутая(не локальная, non local))
# # local(локальная) -> область внутри одной функции

# # a = 10 #global
# # # print built ins
# # def hello(): # global
# #     a = 'hello' # local
# #     print(a, 'local, inside in func!')
# # hello()
# # print(a, ' global')

# # LEGB - LOCAL ENCLOSED GLOBAL BUILT-IN


# # ------------------------------------------------------
# # ENCLOSED - ЗАМкнутое пространство имен - локальное пространство, у которого есть внутреннее(вложенное)
# # локальное пространство

# x = 'global'
# print(x, '1') # global

# def enclosed(): # global
#     x = 'enclosed'
#     def time():
#         s = 'time'
#         print(s,'14')
#     def local(): # enclosed
#         x = 'local'
#         print(x,'3')
#     print(x,'2')#enclosed
#     local()
#     time()
#     print(x,'4')#enclosed
# enclosed()
# print(x,'5') #global


# var = 0
# def increment():
#     global var
#     d = 10
    
#     while var >range(1,10):
#         var = var + 1

# increment()
# print(var)

# global -> позволяет изменять значение глобальной переменной внутри локальной области

#  nonlocal -> позволяет изменять значение не локальной(замкнутой) переменнрй находясь
#  внутри локальной области

def counter(num):
    num = 0
    def increment():
        nonlocal num
        num +=1
        return num
    return increment
c_steps = counter(1)
c_jumps = counter(4)
for _ in range(1, 10000):
    c_steps()

print(c_steps(),c_jumps())
