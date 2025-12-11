from Member import Member

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = 0

    def act(self):
        return f"{self.get_first_name()} {self.get_last_name()} agit en tant que {self.__role}."

    def gain_experience(self):
        self.__experience += 1
    # it's like une reafestation +1

    # --- GETTERS ---
    def get_role(self): return self.__role
    def get_experience(self): return self.__experience

    # --- SETTERS ---
    def set_role(self, new_role): self.__role = new_role
    def set_experience(self, exp):
        if exp >= 0:
            self.__experience = exp
