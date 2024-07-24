import pygame
import random

class Enemy:
    def __init__(self, name, level, health, damage, weaknesses=None, resistances=None, gold_drop=0, item_drops=None):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.weaknesses = weaknesses if weaknesses is not None else []
        self.resistances = resistances if resistances is not None else []
        self.gold_drop = gold_drop
        self.item_drops = item_drops if item_drops is not None else []

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            experience_reward = self.calculate_experience_reward()
            print(f"{self.name} (Level {self.level}) has been defeated! {experience_reward} experience points gained.")


    def calculate_experience_reward(self):
        base_experience = 50  # Base experience reward
        experience_reward = base_experience + (self.level - 1) * 10  # Example formula (adjust as needed)
        return experience_reward


    def is_alive(self):
        return self.health > 0

    def drop_loot(self):
        # Placeholder method for dropping loot
        return 0  # Default to 0 gold dropped
    def __init__(self, image_path, position, window):
        # Load the enemy image from the specified image path
        self.image = pygame.image.load(image_path).convert_alpha()

        # Scale the enemy image to 0.75 times the original size
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.75), int(self.image.get_height() * 0.75)))

        # Set the initial position of the enemy
        self.position = position

        # Set the window where the enemy will be drawn
        self.window = window

        # Set the initial health of the enemy to 100
        self.health = 100

    def take_damage(self, damage):
        # Reduce the enemy's health by the specified damage amount
        self.health -= damage

        # Return True if the enemy's health is less than or equal to 0, indicating that it is defeated
        return self.health <= 0

    def draw(self):
        # Adjust the position to ensure the image does not overflow the window boundaries
        adjusted_position = [
            max(0, min(self.window.get_width() - self.image.get_width(), self.position[0])),
            max(0, min(self.window.get_height() - self.image.get_height(), self.position[1]))
        ]

        # Draw the enemy image on the window at the adjusted position
        self.window.blit(self.image, adjusted_position)

class HealthBar():
  def __init__(self, x, y, w, h, max_hp):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    #calculate health ratio
    ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(250, 200, 300, 40, 100)

run = True
while run:

  screen.fill("indigo")

  #draw health bargit 
  health_bar.hp = 50
  health_bar.draw(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False