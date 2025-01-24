class Character:
  def __init__(self, name, health, magic_points):
      self.name = name
      self.health = health
      self.magic_points = magic_points

  def print_details(self):
      print(f"Name: {self.name}")
      print(f"Health: {self.health}")
      print(f"Magic Points: {self.magic_points}")

class Player(Character):
  def __init__(self, name, health, magic_points, lives):
      super().__init__(name, health, magic_points)
      self.lives = lives

  def is_alive(self):
      return self.health > 0

  def print_details(self):
      super().print_details()
      print(f"Lives: {self.lives}")
      print(f"Alive?: {'Yes' if self.is_alive() else 'No'}")

class Enemy(Character):
  def __init__(self, name, health, magic_points, enemy_type, strength):
      super().__init__(name, health, magic_points)
      self.enemy_type = enemy_type
      self.strength = strength

  def print_details(self):
      super().print_details()
      print(f"Type: {self.enemy_type}")
      print(f"Strength: {self.strength}")

class Orc(Enemy):
  def __init__(self, name, health, magic_points, strength, speed):
      super().__init__(name, health, magic_points, "Orc", strength)
      self.speed = speed

  def print_details(self):
      super().print_details()
      print(f"Speed: {self.speed}")

class Vampire(Enemy):
  def __init__(self, name, health, magic_points, strength, day_night):
      super().__init__(name, health, magic_points, "Vampire", strength)
      self.day_night = day_night

  def print_details(self):
      super().print_details()
      print(f"Day/Night?: {self.day_night}")

# Instantiate characters
player = Player("David", 100, 50, 3)
vampire1 = Vampire("Boris", 45, 70, 3, "Night")
vampire2 = Vampire("Rishi", 70, 10, 75, "Day")
orc1 = Orc("Bill", 60, 5, 75, 90)
orc2 = Orc("Ted", 75, 40, 80, 45)
orc3 = Orc("Station", 35, 40, 49, 50)

# Output the characters
print("\n\u2728 Plus Ultra RPG \u2728\n")
print("Player")
player.print_details()
print("\n" + "-" * 30 + "\n")

for enemy in [vampire1, vampire2, orc1, orc2, orc3]:
  enemy.print_details()
  print("\n" + "-" * 30 + "\n")
