# Each player has a name, a level, and an experience-point total.
# When a player is created, their level should be 1 and their experience points should be 0.
# Implement these methods:
# - __init__(self, name) — Initializes the player's attributes.
# - gain_xp(self, amount) — Adds amount to the player's experience points.
# - level_up(self) — Increases the player's level by 1.
# - show_stats(self) — Prints the player's name, level, and experience points.

class GamePlayer:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0

    def gain_exp(self, amount):
        self.exp += amount

    def level_up(self):
        self.level += 1

    def show_stats(self):
        print(self.name, "is level", self.level, "and", self.exp, "experience points.")

player1 = GamePlayer("Alex")
player2 = GamePlayer("Sam")

player1.gain_exp(150)
player1.level_up()
player2.gain_exp(75)

player1.show_stats()
player2.show_stats()