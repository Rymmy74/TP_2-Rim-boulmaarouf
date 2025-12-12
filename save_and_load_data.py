import json
import ast
from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

def save_data(fleet, file_name="data.json"):
    """
    Sauvegarde la flotte en JSON.
    -------------------------------------------------
    Ici on utilise fleet.__dict__ et les __dict__ des objets
    pour capturer tous les attributs privés (ex: "_Spaceship__shipType").
    """
    json_string = json.dumps(fleet.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    json_dict = ast.literal_eval(json_string)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(json_dict, f, indent=4)
    print("✅ Flotte sauvegardée dans", file_name)


def load_data(file_name="data.json"):
    """
    Recharge la flotte depuis un fichier JSON.
    -------------------------------------------------
    On reconstruit manuellement Fleet, Spaceship, Operator, Mentalist
    en lisant les clés privées (ex: "_Fleet__name").
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    # -- Reconstruction de la flotte --
    fleet_name = data.get("_Fleet__name")
    fleet = Fleet(fleet_name)

    # -- Reconstruction des vaisseaux --
    for ship_data in data.get("_Fleet__spaceships", []):
        ship_name = ship_data.get("_Spaceship__name")
        ship_type = ship_data.get("_Spaceship__shipType", "transport")  # valeur par défaut si absent
        ship_condition = ship_data.get("_Spaceship__condition", 100)    # valeur par défaut si absent
        ship = Spaceship(ship_name, ship_type, ship_condition)

        # -- Reconstruction de l'équipage --
        for member_data in ship_data.get("_Spaceship__crew", []):
            first = member_data.get("_Member__first_name")
            last = member_data.get("_Member__last_name")
            gender = member_data.get("_Member__gender")
            age = member_data.get("_Member__age")

            if "_Operator__role" in member_data:
                role = member_data.get("_Operator__role")
                experience = member_data.get("_Operator__experience", 0)
                member = Operator(first, last, gender, age, role)
                member.set_experience(experience)
            else:
                mana = member_data.get("_Mentalist__mana", 0)
                member = Mentalist(first, last, gender, age)
                member.set_mana(mana)

            ship.append_member(member)

        fleet.append_spaceship(ship)

    print("✅ Flotte chargée depuis", file_name)
    return fleet
