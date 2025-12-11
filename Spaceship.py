from Member import Member
from Operator import Operator
from Mentalist import Mentalist

class Spaceship:
    def __init__(self, name, ship_type, condition="opérationnel"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = []
        self.__condition = condition

    # --- Ajouter un membre ---
    def append_member(self, member):
        if isinstance(member, Member):
            if len(self.__crew) < 10:
                self.__crew.append(member)
            else:
                print("Capacité maximale atteinte (10 membres).")
        else:
            print("Seuls les objets de type Member peuvent être ajoutés.")

    """ def append_member(self, member):
        if isinstance(member, (Operator, Mentalist)):               

            if len(self.__crew) < 10:
                self.__crew.append(member)
            else:
                print("Capacité maximale atteinte (10 membres).")
        else:
            print("Seuls les opérateurs ou mentalistes peuvent être ajoutés.") """

    """ isinstance(obj, Class) → checks if obj is an object created from a certain class.
   Here, member is the object we are testing.
   (Operator, Mentalist) is a tuple of classes.
    So this line means: 👉 “If member is either an Operator OR a Mentalist, then do something """


    def remove_member(self, last_name):
        for m in self.__crew:                          #m stands for member
            if m.get_last_name() == last_name:
                self.__crew.remove(m)
                return
        print(f"Aucun membre nommé {last_name} trouvé.")

    def display_crew(self):   # <-- this is the method main.py is calling
        if not self.__crew:
            print("Aucun membre dans l'équipage.")
        else:
            for m in self.__crew:
                print(m.introduce_yourself())

    def check_preparation(self):
        has_pilot = any(isinstance(m, Operator) and m.get_role() == "pilote" for m in self.__crew)
        has_tech = any(isinstance(m, Operator) and m.get_role() == "technicien" for m in self.__crew)
        has_mentalist = any(isinstance(m, Mentalist) and m.get_mana() >= 50 for m in self.__crew)
        return has_pilot and has_tech and has_mentalist

    def get_name(self): return self.__name
    def get_ship_type(self): return self.__ship_type
    def get_condition(self): return self.__condition
    def get_crew(self): return self.__crew

    # --- Nouvelle méthode pour sauvegarde ---
    def to_dict(self):
        return {
            "name": self.__name,
            "shipType": self.__ship_type,
            "condition": self.__condition,
            "crew": [member.to_dict() for member in self.__crew]
        }

    # --- Nouvelle méthode pour chargement ---
    @staticmethod
    def from_dict(data):
        ship = Spaceship(data["name"], data["shipType"], data["condition"])
        for member_data in data["crew"]:
            if "role" in member_data:  # si c'est un Operator
                member = Operator.from_dict(member_data)
            else:  # sinon c'est un Mentalist
                member = Mentalist.from_dict(member_data)
            ship.append_member(member)
        return ship


""" 
for m in self.__crew → loop through every crew member.
isinstance(m, Operator) → check if the member is an Operator.
m.get_role() == "pilote" → check if their role is "pilote".
any(...) → returns True if at least one member matches.
👉 So this line means: “Is there at least one Operator whose role is 'pilote'?” """

""" 
isinstance(m, Mentalist) → is the member a Mentalist?
m.get_mana() >= 50 → does the Mentalist have enough mana? 
👉 So this line means: “Is there at least one Mentalist with 50 or more mana?”"""


