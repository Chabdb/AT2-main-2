import pygame
from enemy import Enemy
import random

class Map:
    def __init__(self, window):
        """
        Initialize the Map class.
# 1 means physics object
# 0 means non physics object i.e. air
        Args:
            window (pygame.Surface): The game window surface.
        """
        self.window = window
        self.map_image = pygame.image.load("AT2/assets/dungeon_map.png").convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))
        self.player_images = {
            'Warrior': pygame.image.load("AT2/assets/warrior.png").convert_alpha(),
            'Mage': pygame.image.load("AT2/assets/mage.png").convert_alpha(),
            'Rogue': pygame.image.load("AT2/assets/rogue.png").convert_alpha()
        }
        self.player_type = None
        self.player_position = [self.window.get_width() / 2, self.window.get_height() / 2]
        self.enemies = [
            Enemy("AT2/assets/goblin.png", [50, 50], self.window),
            Enemy("AT2/assets/orc.png", [self.window.get_width() - 120, 50], self.window),
            Enemy("AT2/assets/skeleton.png", [50, self.window.get_height() - 120], self.window),
            Enemy("AT2/assets/skeleton.png", [self.window.get_width() - 120, self.window.get_height() - 120], self.window)
        ]
        self.in_combat = False  # Ensure this attribute is defined in the constructor
        self.current_enemy = None
        self.blue_orb = None
        self.game_over = False

class Map:
    def __init__(self, tileMap):
        self.map = tileMap
        self.platform = pygame.image.load('assets/stone.png').convert()
        self.platform =  pygame.transform.scale(self.platform, (16,16))
        self.tile_size = 16
    def load_player(self, character_type):
        """
        Load the player character.
        Args:
            character_type (str): The type of character to load.
        """
        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 0.15), int(self.player_image.get_height() * 0.15)))

    def check_for_combat(self):
        """
        Check if the player is in combat with any enemy.
        Returns:
            bool: True if the player is in combat, False otherwise.
        """
        for enemy in self.enemies:
            if pygame.math.Vector2(enemy.position).distance_to(self.player_position) < 50:
                self.in_combat = True
                self.current_enemy = enemy
                return True
        return False

    def handle_combat(self):
        """
        Handle combat between the player and the current enemy.
        """
        if self.in_combat and self.current_enemy:
            player_damage = random.randint(5, 10)
            enemy_defeated = self.current_enemy.take_damage(player_damage)
            print(f"Player attacks! Deals {player_damage} damage to the enemy.")
            if enemy_defeated:
                print("Enemy defeated!")
                self.enemies.remove(self.current_enemy)
                self.in_combat = False
                self.current_enemy = None
                if not self.enemies:
                    self.spawn_blue_orb()
            else:
                enemy_damage = random.randint(5, 10)
                print(f"Enemy attacks back! Deals {enemy_damage} damage to the player.")
                # Assume player has a method to take damage
                # self.player.take_damage(enemy_damage)

    def spawn_blue_orb(self):
        """
        Spawn the blue orb in the center of the map.
        """
        self.blue_orb = pygame.image.load("AT2/assets/blue_orb.png").convert_alpha()
        self.blue_orb = pygame.transform.scale(self.blue_orb, (50, 50))
        self.orb_position = [self.window.get_width() / 2 - 25, self.window.get_height() / 2 - 25]

    def check_orb_collision(self):
        """
        Check if the player has collided with the blue orb.
        Returns:
            bool: True if the player has collided with the blue orb, False otherwise.
        """
        if self.blue_orb and pygame.math.Vector2(self.orb_position).distance_to(self.player_position) < 25:
            self.game_over = True
            print("YOU WIN")  # This can be modified to a more visual display if needed.
            return True
        return False

    def handle_events(self):
        """
        Handle user input events.
        
        Returns:
            str: 'quit' if the game is over and should be exited, None otherwise.
        """
        if self.game_over:
            return 'quit'  # Stop processing events if game is over

        keys = pygame.key.get_pressed()
        move_speed = 2
        if keys[pygame.K_LEFT]:
            self.player_position[0] -= move_speed
        if keys[pygame.K_RIGHT]:
            self.player_position[0] += move_speed
        if keys[pygame.K_UP]:
            self.player_position[1] -= move_speed
        if keys[pygame.K_DOWN]:
            self.player_position[1] += move_speed

        if not self.in_combat:
            if self.check_for_combat():
                return
        self.handle_combat()

        if self.blue_orb and self.check_orb_collision():
            return 'quit'

    def getCollision(self, pos, size):
        collision = {"up": 0, "left": 0, "right": 0, "down": 0}
        # Check collided with the edges of the map

        if (pos[1] + size[1]) // 16 > len(map) or map[(pos[1] + size[1]) // 16][pos[0] // 16] == 1:
            collision["down"] = 1
        if (pos[1] // 16 < 0) or map[pos[1] // 16] == 1:
            collision["up"] = 1
        if ((pos[0] + size[0]) // 16 > len(map[0])):
            collision["right"] = 1
        if (pos[0] // 16 < 0):
            collision["left"] = 1
        return collision

    def render(self, surf):
        # print(self.map)
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if (int(self.map[i][j]) == 1):
                    surf.blit(self.platform, (self.tile_size*j, self.tile_size*i))
    def draw(self):
        """
        Draw the game objects on the window.
        """
        self.window.fill((0, 0, 0))
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (self.player_position[0], self.player_position[1]))
        for enemy in self.enemies:
            enemy.draw()
        if self.blue_orb:
            self.window.blit(self.blue_orb, self.orb_position)
        pygame.display.flip()