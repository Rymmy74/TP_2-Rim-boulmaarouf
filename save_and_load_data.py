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

    # 1. Conversion de l'objet Fleet en une chaîne JSON
    # - fleet.__dict__ : récupère le dictionnaire interne de l'objet Fleet
    #   (par ex. {"_Fleet__name": "Galactica", "_Fleet__spaceships": [...]})
    # - default=lambda o: o.__dict__ : si json.dumps rencontre un objet
    #   (Spaceship, Operator, Mentalist), il le convertit aussi en dictionnaire
    #   en utilisant son __dict__.
    # - sort_keys=True : trie les clés par ordre alphabétique pour plus de lisibilité.
    # - indent=4 : ajoute une indentation de 4 espaces pour un fichier lisible.
    json_string = json.dumps(fleet.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    # 2. Transformation de la chaîne JSON en dictionnaire Python
    # Ici, on utilise ast.literal_eval pour réinterpréter la chaîne comme un dict.
    # (Remarque : on pourrait aussi utiliser json.loads(json_string), plus classique.)
    json_dict = ast.literal_eval(json_string)

    # 3. Ouverture du fichier en écriture (UTF-8)
    with open(file_name, "w", encoding="utf-8") as f:
        # 4. Écriture du dictionnaire Python dans le fichier au format JSON
        # indent=4 : garde une indentation lisible dans le fichier.
        json.dump(json_dict, f, indent=4)

    # 5. Message de confirmation pour l'utilisateur
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
