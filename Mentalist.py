from Member import Member

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = 100

    def act(self, operator):
        if self.__mana >= 20:
            self.__mana -= 20
            return f"{self.get_first_name()} influence {operator.get_first_name()} {operator.get_last_name()} : {operator.act()}"
        else:
            return f"{self.get_first_name()} n'a pas assez de mana."

    def recharge_mana(self):
        self.__mana = min(100, self.__mana + 50)

    # --- GETTER ---
    def get_mana(self): return self.__mana

    # --- SETTER ---
    def set_mana(self, mana):
        if 0 <= mana <= 100:
            self.__mana = mana

    # --- Nouvelle méthode pour sauvegarde ---
    def to_dict(self):
        return {
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "gender": self.get_gender(),
            "age": self.get_age(),
            "mana": self.__mana
        }

    # --- Nouvelle méthode pour chargement ---
    @staticmethod
    def from_dict(data):
        m = Mentalist(
            data["first_name"],
            data["last_name"],
            data["gender"],
            data["age"]
        )
        m.set_mana(data.get("mana", 100))  # valeur par défaut = 100
        return m
