# class SmartLamp:
#     def __init__(self, color):
#         self.color = color

#     def glow(self):
#         return (f'The lamp glows {self.color}.')
    
#     @property
#     def color(self):
#         return self._color
    
#     @color.setter
#     def color(self, color):
#         if not isinstance(color, str):
#             raise TypeError('Color must be a color name.')
        
#         self._color = color

# class Person:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, str):
#             raise TypeError("Name must be a string type.")
        
#         if new_name == '':
#             raise ValueError("Input string must contain text")
        
#         self._name = new_name

# joe = Person('joe')
# print(joe.name)
# joe.name = ''
# print(joe.name)

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width
    
#     @property
#     def height(self):
#         return self._height

class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with brightness {self.brightness}.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, new_brightness):
        if not isinstance(new_brightness, int):
            raise ValueError('Brightness must be integer')
        
        if new_brightness > 100 or new_brightness < 0:
            raise ValueError('Brightness must be between 0 and 100')
        self._brightness = new_brightness

lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.