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

    def display_crew(self):
        print("\n" + "="*40)
        print(f"👥 Équipage du vaisseau '{self.get_name()}':")
        print("="*40)

        if not self.__crew:
            print("❌ Aucun membre dans l'équipage.")
        else:
            for i, member in enumerate(self.__crew, start=1):
                print(f"\n🔹 Membre {i}")
                print(f"   Nom complet : {member.get_first_name()} {member.get_last_name()}")
                print(f"   Genre       : {member.get_gender()}")
                print(f"   Âge         : {member.get_age()} ans")
                print(f"   Rôle        : {member.get_role()}")

                # -- Affichage spécifique selon le type --
                if isinstance(member, Operator):
                    print(f"   Type        : Opérateur ({member.get_role()})")
                    print(f"   Expérience  : {member.get_experience()} XP")
                elif isinstance(member, Mentalist):
                    print("   Type        : Mentaliste")
                    print(f"   Mana        : {member.get_mana()}")

        print("="*40 + "\n")


    def check_preparation(self):
        reasons = []

        # Vérifier la présence d'un pilote
        has_pilot = any(isinstance(m, Operator) and m.get_role() == "pilote" for m in self.__crew)
        if not has_pilot:
            reasons.append("aucun pilote")

        # Vérifier la présence d'un technicien
        has_tech = any(isinstance(m, Operator) and m.get_role() == "technicien" for m in self.__crew)
        if not has_tech:
            reasons.append("aucun technicien")

        # Vérifier la présence d'un mentaliste avec mana suffisant
        has_mentalist = any(isinstance(m, Mentalist) and m.get_mana() >= 50 for m in self.__crew)
        if not has_mentalist:
            reasons.append("aucun mentaliste avec mana ≥ 50")

        # Retourne True si toutes les conditions sont remplies
        return (len(reasons) == 0, reasons)


    # --- GETTERS ---
    def get_name(self): return self.__name
    def get_ship_type(self): return self.__ship_type
    def get_condition(self): return self.__condition
    def get_crew(self): return self.__crew

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


