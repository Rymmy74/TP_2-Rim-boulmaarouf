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

    fleet = Fleet(data["_Fleet__name"])
    for ship_data in data["_Fleet__spaceships"]:
        ship = Spaceship(ship_data["_Spaceship__name"], ship_data["_Spaceship__shipType"], ship_data["_Spaceship__condition"])
        for member_data in ship_data["_Spaceship__crew"]:
            if "_Operator__role" in member_data:
                member = Operator(member_data["_Member__first_name"], member_data["_Member__last_name"],
                                  member_data["_Member__gender"], member_data["_Member__age"],
                                  member_data["_Operator__role"])
                member.set_experience(member_data["_Operator__experience"])
            else:
                member = Mentalist(member_data["_Member__first_name"], member_data["_Member__last_name"],
                                   member_data["_Member__gender"], member_data["_Member__age"])
                member.set_mana(member_data["_Mentalist__mana"])
            ship.append_member(member)
        fleet.append_spaceship(ship)
    print("✅ Flotte chargée depuis", file_name)
    return fleet
