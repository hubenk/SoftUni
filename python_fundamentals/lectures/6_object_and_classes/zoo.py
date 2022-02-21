class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.fishes.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)} \nTotal animals: {Zoo.__animals}"
        elif species == "fishes":
            return f"Fishes in {self.name}: {', '.join(self.fishes)} \nTotal animals: {Zoo.__animals}"
        elif species == "birds":
            return f"Birds in {self.name}: {', '.join(self.birds)} \nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
number_animals = int(input())

for animal in range(number_animals):
    species, name = input().split()
    zoo.add_animal(species, name)

final_species = zoo.get_info(input())
print(final_species)
