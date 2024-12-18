# class Banner:
#     def __init__(self, message):
#         self.message = message
#         self.len_message = len(self.message)

#     def __str__(self):
#         return "\n".join([self._horizontal_rule(),
#                           self._empty_line(),
#                           self._message_line(),
#                           self._empty_line(),
#                           self._horizontal_rule()])

#     def _empty_line(self):
#         return f"| {self.len_message * ' '} |"

#     def _horizontal_rule(self):
#         if self.len_message == 0:
#             self.len_message = 2
#         return f"+ {self.len_message * '-'} +"

#     def _message_line(self):
#         return f"| {self.message} |"
# # Comments show expected output

# banner = Banner('To boldly go where no one has gone before.')
# print(banner)
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# banner = Banner('')
# print(banner)
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+

# class Rectangle:
#     def __init__(self, width, height):
#         self._height = height 
#         self._width = width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def area(self):
#         return self.height * self.width
    
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

# square = Square(5)
# print(square.area == 25)      # True

# class Pet:
#     def __init__(self, name, age, color):
#         self._name = name
#         self._age = age
#         self._color = color

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @property
#     def color(self):
#         return self._color

#     @property
#     def info(self):
#         return f"My cat {self.name} is {self.age} years old and has {self.color} fur"

# class Cat(Pet):
#     pass

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)

# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")

# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")

# class Cat(Animal):
#     def __init__(self, name, age, status):
#         super().__init__(name, age, 4, 'cat', status)

#     def introduce(self):
#         return super().introduce() + " Meow meow!"

# class Dog(Animal):
#     def __init__(self, name, age, status, owner):
#         super().__init__(name, age, 4, 'dog', status)
#         self.owner = owner

#     def introduce(self):
#         return super().introduce() + " Woof! Woof!"

#     def greet_owner(self):
#         return f"Hi {self.owner}! Woof! Woof!"

# cat = Cat("Pepe", 4, "happy")
# expected = ("Hello, my name is Pepe and I am 4 years old "
#             "and happy. Meow meow!")
# print(cat.introduce() == expected)      # True

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def info(self):
#         return f"{self.make} {self.model}"

# class Car(Vehicle):
#     def get_wheels(self):
#         return 4

# class Motorcycle:
#     def get_wheels(self):
#         return 2

# class Truck:
#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

#     def get_wheels(self):
#         return 6

# class Mammal:
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         return f"{self.name} {self.move_pattern}s forward"

# class Person(Mammal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.move_pattern = 'walk'

# class Cat(Mammal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.move_pattern = 'saunters'

# class Cheetah(Mammal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.move_pattern = 'runs'

# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# class House:
#     def __init__(self, price):
#         self._price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     def __lt__(self, other):
#         if isinstance(other, House):
#             return self.price < other.price

#         return NotImplemented

#     def __gt__(self, other):
#         return self.price > other.price

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

# class Wallet:
#     def __init__(self, amount):
#         self._amount = amount

#     @property
#     def amount(self):
#         return self._amount

#     @amount.setter
#     def amount(self):
#         return self._amount

#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             return Wallet(self.amount + other.amount)

#         return NotImplemented

#     def __str__(self):
#         return f"Wallet with ${self.amount}"

# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.amount == 80)       # True
# print(merged_wallet)          # Wallet with $80.

class Transform:
    def __init__(self, string):
        self._string = string

    @classmethod
    def lowercase(cls, string):
        return string.lower()

    def uppercase(self):
        return self._string.upper()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz