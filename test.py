# protected
# class Student:
#     _schoolName = 'XYZ School' # protected class attribute
    
#     def __init__(self, name, age):
#         self._name=name  # protected instance attribute
#         self._age=age # protected instance attribute

# std = Student("Swati", 25)
# print(std._name)  #'Swati'

# std._name = 'Dipa'
# print(std._name)  #'Dipa'


# # # OR


# class Student:
# 	def __init__(self,name):
# 		self._name = name
# 	@property
# 	def name(self):
# 		return self._name
# 	@name.setter
# 	def name(self,newname):
# 		self._name = newname

# private
# class Student:
#     __schoolName = 'XYZ School' # private class attribute

#     def __init__(self, name, age):
#         self.__name=name  # private instance attribute
#         self.__salary=age # private instance attribute
#     def __display(self):  # private method
# 	    print('This is private method.')

# std = Student("Bill", 25)
# print(std._Student__name)  #'Bill'

# std._Student__name = 'Steve'
# print(std._Student__name)  #'Steve'
# std._Student__display()  #'This is private method.'

# class Animal:
#     def __init__(self, name, speed) -> None:
#         self.name = name
#         self.speed = speed

#     def roar(self):
#         print('ra ra ramama')

# class Lion(Animal):
#     def __init__(self, name, speed) -> None:
#         super().__init__(name, speed)
    
#     def roar(self):
#         print('nya')


# class Cat(Lion, Animal):
#     def __init__(self, name, speed) -> None:
#         super().__init__(name, speed)
    
#     def roar(self):
#         print('kakibara')
#         # return super().roar()
    
# cat = Cat('Gucci', 24)
# cat.roar()


try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Вот и сказочке конец, а кто слушал - молодец.")