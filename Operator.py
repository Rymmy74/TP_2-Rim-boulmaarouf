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

    # --- Nouvelle méthode pour sauvegarde ---
    def to_dict(self):
        return {
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "gender": self.get_gender(),
            "age": self.get_age(),
            "role": self.__role,
            "experience": self.__experience
        }

    # --- Nouvelle méthode pour chargement ---
    @staticmethod
    def from_dict(data):
        op = Operator(
            data["first_name"],
            data["last_name"],
            data["gender"],
            data["age"],
            data["role"]
        )
        op.set_experience(data.get("experience", 0))
        return op
