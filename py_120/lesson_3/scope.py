# class Person:
#     name = 'John'

#     def get_name(self):
#         return self.name
    
# john = Person()
# zack = Person()
# john.name = 'mike'
# zack.name = 'mike'
# print(john.get_name())
# print(zack.get_name())
# print(Person.name)

# class Person:
#     name = 'Leslie'

#     @classmethod
#     def get_name(cls):
#         return [cls.name, Person.name]
    
# class Teacher(Person):
#     name = 'Ms Taylor'

# print(Person.get_name())
# print(Teacher.get_name())

class Person:
    name = 'Leslie'

    def get_name(self):
        return [
            Person.name,
            self.__class__.name,
            type(self).name,
            self.name,
        ]
    
class Teacher(Person):
    name = 'Ms Taylor'

teacher = Teacher()
print(teacher.get_name())