# Анотация свойств (@property(getter setter))

# class Person:
#     __name = 'John'
#     __age = 22

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         return self.__name.title()
#         # return self.__name
    
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             print('Invalid value for name!')
#         else:
#             print(f'setter, {value}')
#             self.__name=value
    
#     @property
#     def age(self):
#         return self.__age
    
# ----------------------------------------------------
# read,write,delete
# class Circle:
#     def __init__(self,radius) -> None:
#         self._radius = radius
    
#     def _get_radius(self):
#         print(f'geeter, _get_radius')
#         return self._radius
    
#     def _set_radius(self,value):
#         print('setter','_set_radius')
#         if not isinstance(value,(int,float)):
#             raise ValueError("Radius must be numeric")  
#         else:
#             self._radius = value
    
#     def _delete_radius(self):
#         answer = input('are you sure yes or no')
#         if answer.lower().strip() == 'yes':
#             del self._radius
#         else:
#             print('not deleted')

#     radius = property(fget = _get_radius, fset= _set_radius,fdel=_delete_radius, doc = 'radius property')
    
# obj = Circle(5)
# print(obj.radius)
# obj.radius = 10
# print(obj.radius)
# del obj.radius


# -----------------------------------------------

# class CoorditaeWriteError(Exception):
#     pass

# class CordinateProperty:
#     def __init__(self,x,y):
#         self._x = x
#         self._y = y

#     @property
#     def _get_coordinates(self):
#         return (self._x,self._y)

#     def _set_coordinates(self,value):
#         if not isinstance(value,tuple) or len(value) !=2 :
#             raise CoorditaeWriteError("Coordinates must be a tuple of two numbers")
#         elif not all(isinstance(i,(int, float)) for i in value):
#             raise CoorditaeWriteError("All elements of the coordinates must be numbers")
    
#     @_get_coordinates.setter
#     def get_coordinates(self,value):
#         raise CoorditaeWriteError('y coordinate is read-only')
#     @_get_coordinates.deleter
#     def remove_coordinates(self):
#         print('Not implemented yet')

# obj = CordinateProperty(42.12123,-12.12313)
# print(obj.get_coordinates)


#---------------------------------------

# import hashlib
# import os

# class User:
#     def __init__(self,username,password) -> None:
#         self.username = username
#         self.__password = password
    
#     @property
#     def password(self):
#         raise AttributeError('Password is write-only!')
    

#     @password.setter
#     def password(self,value):
#         if not isinstance(value,str) or len(value) < 8:
#             raise ValueError('invalid value for password')
#         salt = os.urandom(32)
#         self.__password = hashlib.pbkdf2_hmac('sha256',value.encode('utf-8'),salt,100000)

# john = User('Johns','secretkey')
# # print(john.password)
# john.password = 'JohnSNowThebest'
# print(john._User__password)


#-----------------------------------------------------------------------
