# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, r_name, description):
        self.r_name = r_name
        self.description = description


class subRoom(Room):
    def __init__(self, r_name, description, n_to, s_to, e_to, w_to, sub_des):
        super().__init__(r_name, description)
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.sub_des = sub_des

    # def __init__(self, n_to, s_to, e_to, w_to, sub_des):
    # def __init__(self, n_to, s_to, e_to, w_to, sub_des):
    #     self.n_to = n_to
    #     self.s_to = s_to
    #     self.e_to = e_to
    #     self.w_to = w_to
    #     self.sub_des = sub_des
