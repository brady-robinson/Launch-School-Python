class Todo:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, status):
        if not isinstance(status, bool):
            raise TypeError

        self._done = status

    def __str__(self):
        if self.done == False:
            mark = ' '
        else:
            mark = 'X'

        return f'[{mark}] {self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.done == other.done

def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    print(todo1)                  # [ ] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [ ] Clean room

    print(todo2 == todo4)         # True
    print(todo1 == todo2)         # False
    print(todo4.done)             # False

    todo1.done = True
    todo4.done = True
    print(todo4.done)             # True

    print(todo1)                  # [X] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [X] Clean room

    print(todo2 == todo4)         # False

    todo4.done = False
    print(todo4.done)             # False
    print(todo4)                  # [ ] Clean room

test_todo()