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
