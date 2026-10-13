class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

        print("Initialized:", self.name, "-", self.health)

    def introduce(self):
        print("My name is", self.name)

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def show_status(self):
        print(self.name, "has", self.health, "HP")

player1 = Character("Alex")

player1.take_damage(50)
player1.heal(20)
player1.take_damage(10)

player1.show_status()

