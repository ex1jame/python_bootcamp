from models import Product,Category

def get_all_categories():
    return Category.select(Category.id,Category.title)


def get_all_products():
    return Product.select

print(get_all_categories())
print(get_all_products())

categories = get_all_categories()
print('Vse category')
for category in categories:
    print(f'id: {category} title:{category.title}')


print()
products = get_all_products()
print('Все продукты БД')
for product in products:
    print(f'ID: {product.id},Title: {product.title},Price {product.price}, Category: {product.category_id.title}')


# print('All products in database: ')
# for x in products:
#     print(f'ID: {x.id} Titel: {x.title}, Price: {x.price}, Category: {x.category_id.title}')