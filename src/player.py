# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("There is no cheese that way...")


# Lecture Notes____________________________________________________________________________________________
# class Player:
# ​
#     def __init__(self, name, starting_room):
#         self.name = name
#         self.current_room = starting_room
# ​
#     def travel(self, direction):
#         # Player should be able to move in a direction
#         next_room = self.current_room.get_room_in_direction(direction)
#         if next_room is not None:
#             self.current_room = next_room
#             print(self.current_room)
#         else:
#             print("You cannot move in that direction.")


# Lecture Notes____________________________________________________________________________________________
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
