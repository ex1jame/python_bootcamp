import peewee
from models import Category,Product
import random

def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} - {obj.title}')
    except ( peewee.IntegrityError,peewee.InternalError):
        print(f'{name.lower().strip()} - эта категория уже существует')




def add_product(name,price,category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
    
        print(f'{category,category.title,category.created_at} !!!!!!!')
    except ( peewee.DoesNotExist):
        print(f'{category_name} - этот категория уже существует')
    else:
        obj = Product(title=name, price=price, category_id=category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')




# add_category('laptops')
# add_category('pc')
# add_category('Sony Playstations')
# add_category('Tablets')
# add_category('Smartphone')
# add_category('earphones')

add_product('Macbook AIR 13',800, 'laptops')
add_product('IPhone 7 Plus',2400, 'Smartphone')

add_product('Dell XPS  15',900, 'laptops')
add_product('IPhone 7 Plus',2400, 'Smartphone')