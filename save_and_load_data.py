import json
from Fleet import Fleet

def save_data(fleet, file_name="data.json"):
    """
    Sauvegarde la flotte dans un fichier JSON.
    -------------------------------------------------
    Au lieu d'utiliser fleet.__dict__ (qui expose les
    attributs privés comme "_Spaceship__shipType"),
    on appelle fleet.to_dict().

    Chaque classe (Fleet, Spaceship, Operator, Mentalist)
    sait maintenant se convertir en dictionnaire grâce
    à sa méthode to_dict(). Cela rend le JSON lisible
    et évite les erreurs de KeyError.
    """
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(fleet.to_dict(), f, indent=4)
    print("✅ Flotte sauvegardée dans", file_name)


def load_data(file_name="data.json"):
    """
    Charge une flotte depuis un fichier JSON.
    -------------------------------------------------
    On lit le fichier JSON et on obtient un dictionnaire.
    Ensuite, on appelle Fleet.from_dict(data).

    Grâce aux méthodes from_dict() dans chaque classe :
    - Fleet recrée ses Spaceships
    - Spaceship recrée ses Members
    - Operator et Mentalist recréent leurs attributs

    Résultat : on reconstruit toute la hiérarchie
    d'objets sans manipuler les clés privées.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    fleet = Fleet.from_dict(data)
    print("✅ Flotte chargée depuis", file_name)
    return fleet

