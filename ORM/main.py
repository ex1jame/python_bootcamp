# ORM (object relation mapping) технология программирования блягодаря которой разрабботчик
# могуть использовать язык прошраммирования для взаимодействия с 
# реляционной базой данных(PostgreSQL, MySQL и т д )
# Вместо того чтобы писать сырые запросы операторы sql вы будете писать код на языке прог
# Это очень сильно ускоряет разработку приложения и бд особенно на начальных этапах.

from peewee import PostgresqlDatabase

db= PostgresqlDatabase(
    database='orm_db',
    user='temirlan',
    password='1',
    host="localhost",
    port=5432
) 

# a = db.connect()
# print(a)


