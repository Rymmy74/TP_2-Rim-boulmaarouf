from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist
from save_and_load_data import save_data, load_data
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
        print("3. Supprimer la flotte")   # <-- déplacé ici
        print("4. Ajouter un membre d'équipage")
        print("5. Supprimer un membre d'équipage")
        print("6. Afficher les informations d'un équipage")
        print("7. Vérifier la préparation d'un vaisseau")
        print("8. Sauvegarder la flotte")
        print("9. Afficher les statistiques globales")
        print("10. Déclencher un événement aléatoire")
        print("11. Quitter")

        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                new_name = input("Nouveau nom de la flotte (ou 'cancel') : ")
                if new_name.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue

                choice = input(f"Confirmer le renommage en '{new_name}' ? (o/n) : ")
                if choice.lower() == "o":
                    galactica._Fleet__name = new_name
                    print("✅ Flotte renommée en", new_name)
                    ask_save(galactica)   # <-- utilise la fonction
                else:
                    print("❌ Renommage annulé.")

            case "2":
                # -- Saisie du nom du vaisseau ou annulation --
                name = input("Nom du vaisseau (ou 'cancel') : ")
                if name.lower() == "cancel":
                    print("❌ Ajout annulé.")
                    continue

                # -- Saisie et validation du type --
                valid_types = ["marchand", "guerre", "transport"]
                ship_type = input("Type du vaisseau (marchand/guerre/transport ou 'cancel') : ").lower()
                if ship_type == "cancel":
                    print("❌ Ajout annulé.")
                    continue
                if ship_type not in valid_types:
                    print("❌ Type invalide. Choisissez parmi :", ", ".join(valid_types))
                    continue

                # -- Confirmation avant création --
                choice = input(f"Confirmer l'ajout du vaisseau '{name}' de type '{ship_type}' ? (o/n) : ")
                if choice.lower() == "o":
                    # -- Création et ajout en mémoire --
                    ship = Spaceship(name, ship_type)
                    galactica.append_spaceship(ship)
                    print("✅ Vaisseau ajouté :", name, "de type", ship_type)

                    # -- Sauvegarde (demande séparée) --
                    ask_save(galactica)
                else:
                    # -- Annulation totale : aucune modification --
                    print("❌ Ajout annulé, flotte inchangée.")


            case "3":  # Supprimer la flotte
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ La flotte est déjà vide.")
                    continue

                total_ships = len(fleet_ships)
                total_members = sum(len(ship.get_crew()) for ship in fleet_ships)
                print(f"⚠️ La flotte contient {total_ships} vaisseau(x) et {total_members} membre(s).")

                # -- Confirmation avant suppression --
                choice = input("Voulez-vous vraiment supprimer toute la flotte ? (o/n) : ")
                if choice.lower() == "o":
                    galactica._Fleet__spaceships.clear()
                    print("🗑️ Flotte supprimée avec succès.")

                    # -- Sauvegarde (demande séparée) --
                    ask_save(galactica)
                else:
                    print("❌ Suppression annulée, flotte conservée.")


            case "4":
                    # -- Vérification qu'il y a des vaisseaux --
                    fleet_ships = galactica.get_spaceships()
                    if not fleet_ships:
                        print("❌ Aucun vaisseau dans la flotte.")
                        continue

                    # -- Affichage des vaisseaux disponibles --
                    for i, ship in enumerate(fleet_ships):
                        print(i+1, "-", ship.get_name())

                    # -- Choix du vaisseau --
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

                    # -- Saisie du rôle avec validation stricte --
                    role = input("Type de membre (operator/mentalist ou 'cancel') : ").lower()
                    if role == "cancel":
                        print("❌ Ajout annulé.")
                        continue
                    if role not in ["operator", "mentalist"]:
                        print("❌ Type invalide. Choisissez parmi : operator, mentalist.")
                        continue

                    # -- Saisie prénom et nom --
                    first = input("Prénom (ou 'cancel') : ")
                    if first.lower() == "cancel":
                        print("❌ Ajout annulé.")
                        continue
                    last = input("Nom (ou 'cancel') : ")
                    if last.lower() == "cancel":
                        print("❌ Ajout annulé.")
                        continue

                    # -- Saisie du genre avec validation stricte --
                    gender = input("Genre (femme/homme/autre ou 'cancel') : ").lower()
                    if gender == "cancel":
                        print("❌ Ajout annulé.")
                        continue
                    if gender not in ["femme", "homme", "autre"]:
                        print("❌ Genre invalide. Choisissez parmi : femme, homme, autre.")
                        continue

                    # -- Saisie et validation de l'âge --
                    age_input = input("Âge (ou 'cancel') : ")
                    if age_input.lower() == "cancel":
                        print("❌ Ajout annulé.")
                        continue
                    try:
                        age = int(age_input)
                    except ValueError:
                        print("❌ Âge invalide. Essaie encore.")
                        continue

                    # -- Saisie du rôle spécifique si operator --
                    if role == "operator":
                        op_role = input("Rôle de l'opérateur (pilote/technicien/commandant ou 'cancel') : ").lower()
                        if op_role == "cancel":
                            print("❌ Ajout annulé.")
                            continue
                        if op_role not in ["pilote", "technicien", "commandant"]:
                            print("❌ Rôle invalide. Choisissez parmi : pilote, technicien, commandant.")
                            continue
                        member = Operator(first, last, gender, age, op_role)
                    else:
                        member = Mentalist(first, last, gender, age)

                    # -- Confirmation avant ajout --
                    choice = input(f"Confirmer l'ajout de {first} {last} à '{ship.get_name()}' ? (o/n) : ")
                    if choice.lower() == "o":
                        ship.append_member(member)
                        print("✅ Membre ajouté à", ship.get_name())

                        # -- Sauvegarde (demande séparée) --
                        ask_save(galactica)
                    else:
                        print("❌ Ajout annulé, équipage inchangé.")

            case "5":
                # -- Vérification qu'il y a des vaisseaux --
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue

                # -- Affichage des vaisseaux disponibles --
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())

                # -- Choix du vaisseau --
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

                # -- Saisie du nom du membre à supprimer --
                last_name = input("Nom du membre à supprimer (ou 'cancel') : ")
                if last_name.lower() == "cancel":
                    print("❌ Action annulée.")
                    continue

                # -- Vérification que le membre existe --
                crew = ship.get_crew()
                if not any(m.get_last_name().lower() == last_name.lower() for m in crew):
                    print(f"❌ Aucun membre nommé '{last_name}' dans le vaisseau {ship.get_name()}.")
                    continue

                # -- Confirmation avant suppression --
                choice = input(f"Confirmer la suppression de '{last_name}' ? (o/n) : ")
                if choice.lower() == "o":
                    ship.remove_member(last_name)
                    print("✅ Membre supprimé de", ship.get_name())

                    # -- Sauvegarde (demande séparée) --
                    ask_save(galactica)
                else:
                    print("❌ Suppression annulée, équipage inchangé.")



            case "6":  # Afficher les informations d'un équipage
                # -- Vérification qu'il y a des vaisseaux --
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue

                # -- Affichage des vaisseaux disponibles --
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())

                # -- Choix du vaisseau --
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

                # -- Affichage des informations d'équipage --
                ship = fleet_ships[idx]
                print(f"👥 Équipage du vaisseau '{ship.get_name()}':")
                ship.display_crew()



            case "7":  # Vérifier la préparation d'un vaisseau
                # -- Vérification qu'il y a des vaisseaux --
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue

                # -- Affichage des vaisseaux disponibles --
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())

                # -- Choix du vaisseau --
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

                # -- Vérification de la préparation --
                ship = fleet_ships[idx]
                if ship.check_preparation():
                    print(f"✅ Le vaisseau '{ship.get_name()}' est prêt au départ !")
                else:
                    print(f"❌ Le vaisseau '{ship.get_name()}' n'est pas prêt.")

                        

            case "8":  # Supprimer toute la flotte
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ La flotte est déjà vide.")
                    continue

                total_ships = len(fleet_ships)
                total_members = sum(len(ship.get_crew()) for ship in fleet_ships)
                print(f"⚠️ La flotte contient {total_ships} vaisseau(x) et {total_members} membre(s).")

                # -- Confirmation avant suppression --
                choice = input("Voulez-vous vraiment supprimer toute la flotte ? (o/n) : ")
                if choice.lower() == "o":
                    galactica._Fleet__spaceships.clear()
                    print("🗑️ Flotte supprimée avec succès.")

                    # -- Sauvegarde (demande séparée) --
                    ask_save(galactica)
                else:
                    print("❌ Suppression annulée, flotte conservée.")


            case "9":
                save_data(galactica)
                print("✅ Flotte sauvegardée avec succès.")

            case "10":
                global_statistics(galactica)

            case "11":
                random_event(galactica)

            case "12":
                print("👋 Au revoir !")
                break

            case _:
                print("❌ Choix invalide, réessayez.")

# Lancer le menu
menu()




""" quelque principe :
case 3 :
try → on tente une opération.
Le -1 est nécessaire car en Python les listes commencent à 0, mais toi tu affiches à partir de 1 pour l’utilisateur.
1_except ValueError:
Ce bloc dit : “Si une erreur de type ValueError arrive, ne plante pas le programme. À la place, affiche un message sympa et continue.”
Donc au lieu que ton programme crashe avec un gros message rouge, tu contrôles l’erreur et tu guides l’utilisateur. """