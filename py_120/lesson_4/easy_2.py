# class Game:
#     count = 0
#     def __init__(self):
#         Game.count += 1

#     def play(self):
#         return f'Start the {self.__class__.__name__} game!'

# class Bingo(Game):
#     def __init__(self, game_name, player_name):
#         super().__init__()
#         self.game_name = game_name
#         self.player_name = player_name

# class Scrabble(Game):
#     def __init__(self, game_name, player_name1, player_name2):
#         super().__init__()
#         self.game_name = game_name
#         self.player_name1 = player_name1
#         self.player_name2 = player_name2

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

# class Greeting:
#     def greet(self, message):
#         print(message)

# class Hello(Greeting):

#     @classmethod
#     def hi(cls):
#         greeting = Greeting()
#         greeting.greet('Hello')

# class Goodbye(Greeting):
#     def bye(self):
#         self.greet('Goodbye')

# Hello.hi()

class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>