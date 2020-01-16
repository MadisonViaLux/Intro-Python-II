# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def say_name(self):
        print(self.name, self.current_room)

# class Player:
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs

#     def type(self):
#         print(Player)


# class Child(Player):
#     def __init__(self, name):
#         super().__init__(name, 4)

#     def speak(self):
#         print("hello there")


# me_1 = Player("Madison", 2)

# print(me_1.name)
