# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, r_name, description):
        self.r_name = r_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

     def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None
​
    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits
​
    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"


# Lecture Notes____________________________________________________________________________________________
# class Room:
#     def __init__(self, name, description):
#         # Name, description
#         self.name = name
#         self.description = description
#         # n_to, s_to, e_to, w_to
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None
#         self.items = []
# ​
#     def __str__(self):
#         display_string = ""
#         display_string += f"\n----------------\n"
#         display_string += f"\n{self.name}\n"
#         display_string += f"\n{self.description}\n"
#         display_string += f"\n{self.get_exits_string()}\n"
#         return display_string
# ​
#     def get_room_in_direction(self, direction):
#         if hasattr(self, f"{direction}_to"):
#             return getattr(self, f"{direction}_to")
#         return None
# ​
#     def get_exits(self):
#         exits = []
#         if self.n_to:
#             exits.append("n")
#         if self.s_to:
#             exits.append("s")
#         if self.e_to:
#             exits.append("e")
#         if self.w_to:
#             exits.append("w")
#         return exits
# ​
#     def get_exits_string(self):
#         return f"Exits: {', '.join(self.get_exits())}"



# Group Notes____________________________________________________________________________________________

# class subRoom(Room):
#     def __init__(self, r_name, description, n_to, s_to, e_to, w_to, sub_des):
#         super().__init__(r_name, description)
#         self.n_to = n_to
#         self.s_to = s_to
#         self.e_to = e_to
#         self.w_to = w_to
#         self.sub_des = sub_des

    # def __init__(self, n_to, s_to, e_to, w_to, sub_des):
    # def __init__(self, n_to, s_to, e_to, w_to, sub_des):
    #     self.n_to = n_to
    #     self.s_to = s_to
    #     self.e_to = e_to
    #     self.w_to = w_to
    #     self.sub_des = sub_des
