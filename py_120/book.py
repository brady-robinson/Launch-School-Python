# class GoodDog:
#     def __init__(self, name):
#         self.name = name
#         print(f"Constructor for {self.name}")

#     def speak(self):
#         print(f"{self.name} says Woof!")
    
#     def roll_over(self):
#         print(f"{self.name} is rolling over")

# sparky = GoodDog('Sparky')
# sparky.speak()
# sparky.roll_over()

# class Pet:
#     def __init__(self, name):
#         self.name = name
#         type_name = self.__class__.__name__
#         print(f'I am {self.name} and {type_name}')

#     def eat(self):
#         print(f'{self.name}: Yum-yum-yum!')

# class Dog(Pet):
#     def speak(self):
#         print(f"{self.name} says Woof!")
    
#     def roll_over(self):
#         print(f"{self.name} is rolling over")

# class Cat(Pet):
#     def speak(self):
#         print(f"{self.name} says Meow!")

# class Parrot(Pet):
#     def speak(self):
#         print(f"{self.name} wants a cracker!")

# sparky = Dog('sparky')
# fluffy = Cat('fluffy')
# polly = Parrot('polly')

# for animal in [sparky, fluffy, polly]:
#     animal.speak()
#     animal.eat()

# class Foo:
#     def __init__(self, id):
#         self.id = id
#         class_name = self.__class__.__name__
#         print(f'I am a {class_name} object')

# foo = Foo(123)

# class GoodDog:

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#         print("this object was initialized")

#     def name(self):
#         return self._name

#     def set_name(self, new_name):
#         if not isinstance(new_name, str):
#             raise TypeError('Name must be a string')
#         self._name = new_name

#     def speak(self):
#         return f"{self._name} says Arf!"

#     def age(self):
#         return self._age

#     def set_age(self, new_age):
#         if not isinstance(new_age, int):
#             raise TypeError('Age must not be integer')
#         if new_age < 0:
#             raise ValueError("Age can't be negative")

#         self._age = new_age

# sparky = GoodDog('Sparky', 5)
# sparky.speak()
# print(sparky.name())
# print(sparky.age())
# sparky.set_name('Fireplug')
# print(sparky.name())

# class GoodCat:

#     @classmethod
#     def what_am_i(cls):
#         print("I'm a GoodCat class!")

#     @classmethod
#     def who_am_i(cls):
#         print("Who am I?")
#         cls.what_am_i()

# GoodCat.who_am_i()

# class Foo1:

#     @classmethod
#     def bar(cls):
#         print("this is bar in Foo1")

#     def qux(self):
#         self.__class__.bar()

# class Foo2(Foo1):

#     @classmethod
#     def bar(cls):
#         print("this is bar in Foo2")

# foo1 = Foo1()
# foo1.qux()
# foo2 = Foo2()
# foo2.qux()

# class GoodCat:
#     counter = 0

#     def __init__(self):
#         GoodCat.counter += 1

#     @classmethod
#     def number_of_cats(cls):
#         return GoodCat.counter

# class ReallyGoodCat(GoodCat):
#     pass

# cat1 = GoodCat()
# cat2 = GoodCat()
# cat3 = ReallyGoodCat()

# print(GoodCat.number_of_cats())
# print(GoodCat.counter)
# print(ReallyGoodCat.number_of_cats())
# print(ReallyGoodCat.counter)

# class GoodCat:
#     CAT_YEARS = 5

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def human_age(self):
#         return self.age * GoodCat.CAT_YEARS

# cocoa = GoodCat('Cocoa', 4)
# print(cocoa.human_age())

# class Car:

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
    #     self.speed = 0
    #     self.engine_on = False

    # @property
    # def model(self):
    #     return self._model

    # @property
    # def year(self):
    #     return self._year

    # @property
    # def color(self):
    #     return self._color

    # @color.setter
    # def color(self, color):
    #     self._color = color
    
    # def turn_engine_one(self):
    #     if self.engine_on == True:
    #         return 'Engine is already on'
        
    #     self.engine_on = True
    #     return 'You have turned the engine on.'

    # def accelerate(self, amount):
    #     if self.engine_on == False:
    #         return 'First you need to turn the engine one'
    #     self.speed += amount
    #     return f'Current speed is now {self.speed}'

    # def brake(self, amount):
    #     if self.engine_on == False:
    #         return 'First you need to turn the engine one'

    #     if self.speed == 0:
    #         return 'You are already stopped'

    #     self.speed = max(self.speed - amount, 0)
    #     return f'Current speed is now {self.speed}'

    # def turn_engine_off(self):
    #     if self.engine_on == False:
    #         return 'Engine is already off.'

    #     self.engine_on = False
    #     return 'You have turned the engine off.'

    # def display_speed(self):
    #     print(f'Current speed: {self.speed}')

    # def paint_new_color(self, new_color):
    #     self.color = new_color

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return f'Cat({repr(self.name)})'

# kitty = Cat('kitty')
# print(str(kitty))
# print(repr(kitty))

# import mod1
# import mod2

# print(__name__)

# import os

# print(__file__)
# print(os.path.abspath(__file__))

# class MyClass:
#     def __init__(self, x):
#         self.x = x
#         self.y = []
#         self.z = 'xxx'

# obj = MyClass(5)
# print(obj.__dict__)

# class Car:
#     def __init__(self, name, year, color):
#         self.name = name
#         self.year = year
#         self.color = color

#     def __str__(self):
#         return f'{self.color} {self.year} {self.name}'
    
#     def __repr__(self):
#         return f'Car({repr(self.name)}, {repr(self.year)}, {repr(self.color)})'

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

# class Candidate:
#     def __init__(self, name):
#         self.name = name
#         self.votes = 0

#     def __iadd__(self, num):
#         self.votes += num

#     def get_votes(self):
#         return self.votes
    
#     def get_name(self):
#         return self.name

# class Election:
#     def __init__(self, candidates):
#         self.candidates = candidates

#     def results(self):
#         tally = []
#         total_votes = 0
#         for c in self.candidates:
#             print(f'{c.get_name()}: {c.get_votes()} votes')
#             total_votes += c.get_votes()
#             tally.append([c.get_name(), c.get_votes()])

#         tally = [[t[0],(t[1]/total_votes)*100] for t in tally]
#         tally.sort(key=lambda x: x[1], reverse=True)
#         print(f'{tally[0][0]} won: {tally[0][1]}% of votes')

# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()

# class TurnSignalMixin:
#     def signal_left(self):
#         print("Signalling left")

#     def signal_right(self):
#         print("Signalling right")

#     def signal_off(self):
#         print("Signal off")

# class Vehicle:
#     num_vehicles = 0

#     def __init__(self):
#         Vehicle.num_vehicles += 1

#     @classmethod
#     def vehicles(cls):
#         return Vehicle.num_vehicles

# class Car(TurnSignalMixin, Vehicle):
#     def __init__(self):
#         super().__init__()

# class Truck(TurnSignalMixin, Vehicle):
#     def __init__(self):
#         super().__init__()

# class Boat(Vehicle):
#     def __init__(self):
#         super().__init__()

# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# # boat1.signal_left()
# # AttributeError: 'Boat' object has no attribute
# # 'signal_left'

# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro())
# class Vehicle:
#     def __init__(self, fuel_capacity, mpg):
#         self.fuel_capacity = fuel_capacity
#         self.mpg = mpg

#     def max_range_in_miles(self):
#         return self.fuel_capacity * self.mpg

# class Car(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def family_drive(self):
#         print('Taking the family for a drive')

# class Truck(Vehicle):

#     def __init__(self, fuel_capacity, mpg):
#         super().__init__(fuel_capacity, mpg)

#     def hookup_trailer(self):
#         print('Hooking up trailer')

# car = Car(12.5, 25.4)
# truck = Truck(150.0, 6.25)

# print(car.max_range_in_miles())         # 317.5
# print(truck.max_range_in_miles())       # 937.5

# car.family_drive()     # Taking the family for a drive
# truck.hookup_trailer() # Hooking up trailer

# try:
#     truck.family_drive()
# except AttributeError:
#     print('No family_drive method for Truck')
# # No family_drive method for Truck

# try:
#     car.hookup_trailer()
# except AttributeError:
#     print('No hookup_trailer method for Car')
# # No hookup_trailer method for Car