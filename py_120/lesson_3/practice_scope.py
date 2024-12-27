# class Dog:
#     def __init__(self, breed):
#         self._breed = breed

#     def get_breed(self):
#         return self._breed

# gold = Dog("Golden Retriever")
# poodle = Dog("Poodle")
# poodle._breed = 'Yorkie'
# print(gold.get_breed())
# print(poodle.get_breed())

# class Cat:
#     def __init__(self, name=False):
#         self.name = name

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         if not isinstance(self.name, str):
#             print('Name not set!')

#         return self.name

# class Student:
#     school_name = 'Oxford'

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_school(cls):
#         return cls.school_name

# print(Student.get_school())
# print(Student.school_name)

# class Car:
#     manufacturer = 'Ford'

#     def __init__(self, man):
#         self.manufacturer = man

#     def show_manufacturer(self):
#         print(f'{self.manufacturer=}')
#         print(f'{Car.manufacturer=}')

# honda = Car('honda')
# honda.show_manufacturer()

# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     pass

# sparrow = Sparrow('sparrow')
# print(sparrow.species)

