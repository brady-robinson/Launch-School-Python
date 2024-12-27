# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name
    
# class SwimMixin:
#     def enable_swimming(self):
#         self.can_swim = True

#     def can_i_swim(self):
#         if not hasattr(self, 'can_swim'):
#             self.can_swim = False

#         return self.can_swim
    
# class Dog(SwimMixin, Animal):
#     def __init__(self, name):
#         # super().__init__(name)
#         self.name = name

#     def speak(self):
#         return f'bark! bark! {self.name} bark! bark!'
    
#     def swim(self):
#         if self.can_i_swim():
#             print('i am swimming')
    
# sparky = Dog('sparky')
# print(sparky.speak())
# print(sparky.get_name())
# sparky.swim()
# sparky.enable_swimming()
# sparky.swim()

class Animal:
    total_animals = 0

    def __init__(self):
        self.__class__.total_animals += 1

class Dog(Animal):
    def animal_count(self):
        return self.__class__.total_animals
    
spike = Dog()
print(spike.total_animals)
print(spike.animal_count())