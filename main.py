from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

# Créer une flotte
galactica = Fleet("Galactica")

def menu():
    while True:
        print("\n=== Gestion de la flotte :", galactica.get_name(), "===")
        print("1. Renommer la flotte")
        print("2. Ajouter un vaisseau à la flotte")
        print("3. Ajouter un membre d'équipage")
        print("4. Supprimer un membre d'équipage")
        print("5. Afficher les informations d'un équipage")
        print("6. Vérifier la préparation d'un vaisseau")
        print("7. Afficher les statistiques de la flotte")
        print("8. Quitter")

        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                new_name = input("Nouveau nom de la flotte : ")
                galactica._Fleet__name = new_name  # setter simplifié
                print("✅ Flotte renommée en", new_name)

            case "2":
                name = input("Nom du vaisseau : ")
                ship_type = input("Type du vaisseau (marchand/guerre/transport) : ")
                ship = Spaceship(name, ship_type)
                galactica.append_spaceship(ship)
                print("✅ Vaisseau ajouté :", name)

            case "3":
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx = int(input("Choisissez un vaisseau : ")) - 1
                ship = fleet_ships[idx]

                role = input("Type de membre (operator/mentalist) : ")
                first = input("Prénom : ")
                last = input("Nom : ")
                gender = input("Genre : ")
                age = int(input("Âge : "))

                if role == "operator":
                    op_role = input("Rôle de l'opérateur (pilote/technicien/commandant) : ")
                    member = Operator(first, last, gender, age, op_role)
                else:
                    member = Mentalist(first, last, gender, age)

                ship.append_member(member)
                print("✅ Membre ajouté à", ship.get_name())

            case "4":
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx = int(input("Choisissez un vaisseau : ")) - 1
                ship = fleet_ships[idx]
                last_name = input("Nom du membre à supprimer : ")
                ship.remove_member(last_name)

            case "5":
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx = int(input("Choisissez un vaisseau : ")) - 1
                ship = fleet_ships[idx]
                ship.display_crew()

            case "6":
                fleet_ships = galactica.get_spaceships()
                if not fleet_ships:
                    print("❌ Aucun vaisseau dans la flotte.")
                    continue
                for i, ship in enumerate(fleet_ships):
                    print(i+1, "-", ship.get_name())
                idx = int(input("Choisissez un vaisseau : ")) - 1
                ship = fleet_ships[idx]
                if ship.check_preparation():
                    print("✅ Le vaisseau est prêt au départ !")
                else:
                    print("❌ Le vaisseau n'est pas prêt.")

            case "7":
                galactica.statistics()

            case "8":
                print("👋 Au revoir !")
                break

            case _:
                print("❌ Choix invalide, réessayez.")

# Lancer le menu
menu()


