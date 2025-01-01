# print(type(True))
# print(True.__class__.__name__)
# print('hello'.__class__)
# print(type(142))

# class AngryCat:
#     def hiss(self):
#         print('Hisssss!!!')

# cat = AngryCat()

# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}')

# class Car(SpeedMixin):
#     def go_slow(self):
#         print('I am safe and driving slow.')

# class Truck(SpeedMixin):
#     def go_very_slow(self):
#         print('I am a heavy truck and like going very slow.')

# chevy = Truck()
# chevy.go_fast()
# for klass in Truck.mro():
#     print(klass)
# print(vars(chevy))

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

print(Cat.cats_count())
cat1 = Cat('furry')
print(Cat.cats_count())
cat2 = Cat('hairy')
print(Cat.cats_count())