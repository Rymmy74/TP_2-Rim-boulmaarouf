from Spaceship import Spaceship
class Fleet:
    def __init__(self, name):
        self.__name = name
        self.__spaceships = []

    # --- Ajouter un vaisseau ---
    def append_spaceship(self, ship: Spaceship):
        if len(self.__spaceships) < 15:
            self.__spaceships.append(ship)
        else:
            print("Capacité maximale atteinte (15 vaisseaux).")

    # --- Statistiques ---
    def statistics(self): 
        total_members = sum(len(ship.get_crew()) for ship in self.__spaceships)
        total_ships = len(self.__spaceships)
        print(f"Flotte {self.__name} contient {total_ships} vaisseaux et {total_members} membres.")

        """ self.__spaceships → it's the liste of all the spaceships in the fleet.
         ship.get_crew() → get the crew of the spaceship (it's a liste of members).
         len(ship.get_crew()) → how many members are in the spaceship
         sum(...) → sums all the members that are present in the flotte. """

    # --- GETTERS ---
    def get_name(self): return self.__name
    def get_spaceships(self): return self.__spaceships

    # --- Nouvelle méthode pour sauvegarde ---
    def to_dict(self):
        return {
            "name": self.__name,
            "spaceships": [ship.to_dict() for ship in self.__spaceships]
        }

    # --- Nouvelle méthode pour chargement ---
    @staticmethod
    def from_dict(data):
        from Spaceship import Spaceship
        fleet = Fleet(data["name"])
        for ship_data in data["spaceships"]:
            fleet.append_spaceship(Spaceship.from_dict(ship_data))
        return fleet

