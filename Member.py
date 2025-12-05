class Member:
    def __init__(self, first_name, last_name, gender, age):
        # Attributs encapsulés (privés)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    def introduce_yourself(self):
        return f"Je m'appelle {self.__first_name} {self.__last_name}, je suis un(e) {self.__gender} de {self.__age} ans."

# --- GETTERS ---
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

# --- SETTERS ---
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_gender(self, new_gender):
        self.__gender = new_gender

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
