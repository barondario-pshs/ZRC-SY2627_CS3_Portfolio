
class PSHS_GALAXY:
    def __init__(self):
        self.galaxy_name = "PSHS_GALAXY"

        self.directory = {}

class Nationality(PSHS_GALAXY):
    def __init__(self):
        super().__init__()
        self.subgroups = {
            "Filipinos": [],
            "Indonesians": [],
            "Spaniards": []
        }

class Alien(PSHS_GALAXY):
    def __init__(self):
        super().__init__()
        self.subgroups = {
            "Marvel": [],
            "Avengers": []
        }

class Filipinos(Nationality):
    def add(self, name):
        self.subgroups["Filipinos"].append(name)

class Indonesians(Nationality):
    def add(self, name):
        self.subgroups["Indonesians"].append(name)

class Spaniards(Nationality):
    def add(self, name):
        self.subgroups["Spaniards"].append(name)

class Marvel(Alien):
    def add(self, name):
        self.subgroups["Marvel"].append(name)

class Avengers(Alien):
    def add(self, name):
        self.subgroups["Avengers"].append(name)