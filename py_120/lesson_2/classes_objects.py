# class Person:
#     def __init__(self, first_name, last_name=''):
#         self.first_name = first_name
#         self.last_name = last_name

#     @property
#     def name(self):
#         return self.first_name + ' ' + self.last_name
    
#     @name.setter
#     def name(self, name):
#         if len(name.split()) == 1:
#             self.first_name = name
#             self.last_name = ''
#         else:
#             name = name.split()
#             self.first_name = name[0]
#             self.last_name = name[1]

#         self._name = self.first_name + ' ' + self.last_name

# bob = Person('Robert Smith')
# rob = Person('Robert Smith')
# print(bob.name == rob.name)

# Comments show expected output
# print(type("Hello"))               # <class 'str'>
# print(type(5))                      # <class 'int'>
# print(type([1, 2, 3]))              # <class 'list'>

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     def greet(self):
#         print(f"I'm a {self.name}")

# kitty = Cat('sophie')
# kitty.greet()
# kitty.name = 'Luna'
# kitty.greet()

# class Person:
#     def __init__(self, name='John Doe'):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

# person1 = Person()
# person2 = Person("Pepe Le Pew")

# # Comments show expected output
# print(person1.name)    # John Doe
# print(person2.name)    # Pepe Le Pew

# class Cat:
#     def __init__(self):
#         pass
    
#     @classmethod
#     def generic_greeting(cls):
#         print("I'm a cat!")

# Cat.generic_greeting()
# kitty = Cat()
# print(type(kitty))#.generic_greeting()

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     def rename(self, new_name):
#         self.name = new_name

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.name)             # Sophie
# kitty.rename('Chloe')
# print(kitty.name)             # Chloe

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     def identify(self):
#         return self


# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty.identify())
# # <__main__.Cat object at 0x10508c8d0>
# # The object ID (0x105...) may vary

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def personal_greeting(self):
#         print(f'Hello! My name is {self.name}')

# kitty = Cat('Sophie')
# kitty.personal_greeting()     # Hello! My name is Sophie!

# class Cat:
#     num_objects_instantiated = 0

#     def __init__(cls):
#         Cat.num_objects_instantiated += 1

#     @classmethod
#     def total(cls):
#         print(cls.num_objects_instantiated)

# Cat.total()         # 0

# kitty1 = Cat()
# Cat.total()         # 1

# kitty2 = Cat()
# Cat.total()         # 2

# print(Cat())        # <__main__.Cat object at 0x104ed7290>
# Cat.total()         # 3

# class Cat:
#     COLOR = 'purple'

#     def __init__(self, name='Sophie'):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     def greet(self):
#         print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")

# s = Cat()
# s.greet()

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def __str__(self):
#         return f'i am {self._name}'

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty)        # I'm Sophie!

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!