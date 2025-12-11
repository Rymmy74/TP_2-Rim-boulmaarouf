from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist
from save_and_load_date import save_data, load_data
import random

# --- Fonction utilitaire pour proposer la sauvegarde ---
def ask_save(fleet):
    choice = input("Voulez-vous sauvegarder la flotte ? (o/n) : ")
    if choice.lower() == "o":
        save_data(fleet)

# --- Chargement au démarrage ---
galactica = Fleet("Galactica")
start_choice = input("Voulez-vous charger une flotte existante ? (o/n) : ")
if start_choice.lower() == "o":
    galactica = load_data("data.json")

# --- Événement aléatoire ---
def random_event(fleet):
    event = random.choice(["attaque", "renfort"])
    if event == "attaque" and fleet.get_spaceships():
        ship = random.choice(fleet.get_spaceships())
        ship._Spaceship__condition = "endommagé"
        print(f"⚠️ Attaque ennemie ! Le vaisseau {ship.get_name()} est endommagé.")
    elif event == "renfort" and fleet.get_spaceships():
        ship = random.choice(fleet.get_spaceships())
        new_member = Operator("Renfort", "Inconnu", "homme", 25, "technicien")
        ship.append_member(new_member)
        print(f"🛠️ Renfort ajouté au vaisseau {ship.get_name()}.")

# --- Statistiques globales ---
def global_statistics(fleet):
    total_ships = len(fleet.get_spaceships())
    roles = {"pilote":0, "technicien":0, "commandant":0, "mentaliste":0}
    operational = 0
    damaged = 0

    for ship in fleet.get_spaceships():
        if ship.get_condition() == "opérationnel":
            operational += 1
        else:
            damaged += 1
        for m in ship.get_crew():
            if isinstance(m, Operator):
                roles[m.get_role()] = roles.get(m.get_role(), 0) + 1
            elif isinstance(m, Mentalist):
                roles["mentaliste"] += 1

    print(f"📊 Statistiques globales :")
    print(f"- Nombre total de vaisseaux : {total_ships}")
    print(f"- Membres par rôle : {roles}")
    print(f"- Vaisseaux opérationnels : {operational}, endommagés : {damaged}")

# --- Menu principal ---
def menu():
    global galactica
    while True:
        print("\n=== Gestion de la flotte :", galactica.get_name(), "===")
        print("1. Renommer la flotte")
        print("2. Ajouter un vaisseau à la flotte")
        print("3. Ajouter un membre d'équipage")
        print("4. Supprimer un membre d'équipage")
        print("5. Afficher les informations d'un équipage")
        print("6. Vérifier la préparation d'un vaisseau")
        print("7. Sauvegarder la flotte")
        print("8. Afficher les statistiques globales")
        print("9. Déclencher un événement aléatoire")
        print("10. Quitter")

        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                new_name = input("Nouveau nom de la flotte (ou 'cancel') : ")
                if new_name.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue
                galactica._Fleet__name = new_name
                print("✅ Flotte renommée en", new_name)
                ask_save(galactica)

            case "2":
                name = input("Nom du vaisseau (ou 'cancel') : ")
                if name.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                valid_types = ["marchand", "guerre", "transport"]
                ship_type = input("Type du vaisseau (marchand/guerre/transport ou 'cancel') : ").lower()
                if ship_type == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                if ship_type not in valid_types:
                    print("❌ Type invalide. Choisissez parmi :", ", ".join(valid_types))
                    continue
                ship = Spaceship(name, ship_type)
                galactica.append_spaceship(ship)
                print("✅ Vaisseau ajouté :", name, "de type", ship_type)
                ask_save(galactica)

            case "3":  # Ajouter un membre d'équipage
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx_input = input("Choisissez un vaisseau (ou 'cancel') : ")
                if idx_input.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                try:
                    idx = int(idx_input) - 1
                except ValueError:
                    print("😅 Oups ! Ce n'était pas un numéro. Essaie encore.")
                    continue
                if idx < 0 or idx >= len(fleet_ships):
                    print("❌ Numéro invalide. Essaie encore.")
                    continue
                ship = fleet_ships[idx]

                role = input("Type de membre (operator/mentalist ou 'cancel') : ")
                if role.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                first = input("Prénom (ou 'cancel') : ")
                if first.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                last = input("Nom (ou 'cancel') : ")
                if last.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                gender = input("Genre (ou 'cancel') : ")
                if gender.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                age_input = input("Âge (ou 'cancel') : ")
                if age_input.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                try:
                    age = int(age_input)
                except ValueError:
                    print("❌ Âge invalide. Essaie encore.")
                    continue

                if role == "operator":
                    op_role = input("Rôle de l'opérateur (pilote/technicien/commandant ou 'cancel') : ")
                    if op_role.lower() == "cancel":
                        print("❌ Ajout annulé.")
                        continue
                    member = Operator(first, last, gender, age, op_role)
                else:
                    member = Mentalist(first, last, gender, age)

                ship.append_member(member)
                print("✅ Membre ajouté à", ship.get_name())
                ask_save(galactica)


            case "4":  # Supprimer un membre d'équipage
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx_input = input("Choisissez un vaisseau (ou 'cancel') : ")
                if idx_input.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue
                try:
                    idx = int(idx_input) - 1
                except ValueError:
                    print("😅 Oups ! Ce n'était pas un numéro. Essaie encore.")
                    continue
                if idx < 0 or idx >= len(fleet_ships):
                    print("❌ Numéro invalide. Essaie encore.")
                    continue
                ship = fleet_ships[idx]
                last_name = input("Nom du membre à supprimer (ou 'cancel') : ")
                if last_name.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue
                ship.remove_member(last_name)
                ask_save(galactica)


            case "5":  # Afficher les informations d'un équipage
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx_input = input("Choisissez un vaisseau (ou 'cancel') : ")
                if idx_input.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue
                try:
                    idx = int(idx_input) - 1
                except ValueError:
                    print("😅 Oups ! Ce n'était pas un numéro. Essaie encore.")
                    continue
                if idx < 0 or idx >= len(fleet_ships):
                    print("❌ Numéro invalide. Essaie encore.")
                    continue
                ship = fleet_ships[idx]
                ship.display_crew()


            case "6":  # Vérifier la préparation d'un vaisseau
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx_input = input("Choisissez un vaisseau (ou 'cancel') : ")
                if idx_input.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue
                try:
                    idx = int(idx_input) - 1
                except ValueError:
                    print("😅 Oups ! Ce n'était pas un numéro. Essaie encore.")
                    continue
                if idx < 0 or idx >= len(fleet_ships):
                    print("❌ Numéro invalide. Essaie encore.")
                    continue
                ship = fleet_ships[idx]
                if ship.check_preparation():
                    print("✅ Le vaisseau est prêt au départ !")
                else:
                    print("❌ Le vaisseau n'est pas prêt.")


            case "7":
                save_data(galactica)

            case "8":
                global_statistics(galactica)

            case "9":
                random_event(galactica)

            case "10":
                print("👋 Au revoir !")
                break

            case _:
                print("❌ Choix invalide, réessayez.")

# Lancer le menu
menu()
