from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

# Créer une flotte
from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

# Créer une flotte
galactica = Fleet("Galactica")

# Créer deux vaisseaux
ship1 = Spaceship("Bayta", "marchand")
ship2 = Spaceship("Raven", "guerre")

# Ajouter des membres
ship1.append_member(Operator("Bayta", "Darell", "femme", 28, "pilote"))
ship1.append_member(Operator("Gaal", "Dornick", "femme", 34, "technicien"))
ship1.append_member(Mentalist("Hari", "Seldon", "homme", 60))

ship2.append_member(Operator("Bel", "Riose", "homme", 48, "commandant"))

# Ajouter les vaisseaux à la flotte
galactica.append_spaceship(ship1)
galactica.append_spaceship(ship2)

# Afficher les infos
ship1.display_crew()
if ship1.check_preparation():
    print("✅ Le vaisseau Bayta est prêt au départ !")
else:
    print("❌ Le vaisseau Bayta n'est pas prêt.")

galactica.statistics()

# Exemple d'interaction Mentalist → Operator
mentalist = ship1.get_crew()[2]   # Hari Seldon
operator = ship1.get_crew()[0]    # Bayta Darell
print(mentalist.act(operator))



