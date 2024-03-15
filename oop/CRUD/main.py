from views import CreateMixin,ReadMixin

class Smartphones(CreateMixin,ReadMixin):
    pass

    
obj = Smartphones()
obj.post(title='Redmi Note 10',description='The best phone for own price!',qty=10,price=250)
obj.post(title='Xiomi',description='The best phone for own price!',qty=10,price=250)
obj.post(title='Samsung',description='The best phone for own price!',qty=10,price=250)
obj.post(title='lenova',description='The best phone for own price!',qty=10,price=250)
obj.post(title='Iphone',description='The best phone for own price!',qty=10,price=250)

print(*obj.list()['msg'], sep='\n')
print(obj.list())
print()
print(obj.detail(1))