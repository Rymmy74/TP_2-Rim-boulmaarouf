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


    def remove_member(self, last_name):
        for m in self.__crew:  # m stands for member
            if m.get_last_name() == last_name:
                self.__crew.remove(m)
                return
        print(f"Aucun membre nommé {last_name} trouvé.")

    def display_crew(self):   # <-- méthode appelée dans main.py
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

    # --- GETTERS ---
    def get_name(self): return self.__name
    def get_ship_type(self): return self.__ship_type
    def get_condition(self): return self.__condition
    def get_crew(self): return self.__crew
    
    # --- SETTERS ---
    def set_name(self, new_name):
        self.__name = new_name

    def set_ship_type(self, new_type):
        self.__ship_type = new_type

    def set_condition(self, new_condition):
        self.__condition = new_condition

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


