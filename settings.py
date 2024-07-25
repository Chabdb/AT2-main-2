import pygame
import sys

class SettingsPage:
    def __init__(self, window, font, background_image):
        self.window = window
        self.font = font
        self.background_image = background_image

        # Button colours
        self.button_background = (0, 0, 0)
        self.button_text_colour = (255, 255, 255)

        # Set up the buttons
        self.music_button = pygame.Rect(325, 200, 150, 50)
        self.controls_button = pygame.Rect(325, 300, 150, 50)
        self.graphics_button = pygame.Rect(325, 400, 150, 50)
        self.back_button = pygame.Rect(325, 500, 150, 50)
# settings.py

    def draw_button(self, rect, label):
        pygame.draw.rect(self.window, self.button_background, rect)
        text = self.font.render(label, True, self.button_text_colour)
        text_rect = text.get_rect(center=rect.center)
        self.window.blit(text, text_rect)
class Settings:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 36)
        self.options = ["Volume", "Graphics", "Back"]
        self.selected_option = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.music_button.collidepoint(mouse_x, mouse_y):
                        print("Music settings clicked")
                    elif self.controls_button.collidepoint(mouse_x, mouse_y):
                        print("Controls settings clicked")
                    elif self.graphics_button.collidepoint(mouse_x, mouse_y):
                        print("Graphics settings clicked")
                    elif self.back_button.collidepoint(mouse_x, mouse_y):
                        return

            self.window.blit(self.background_image, (0, 0))

            self.draw_button(self.music_button, "Music")
            self.draw_button(self.controls_button, "Controls")
            self.draw_button(self.graphics_button, "Graphics")
            self.draw_button(self.back_button, "Back")
            self.window.fill((0, 0, 0))
            for index, option in enumerate(self.options):
                color = (255, 0, 0) if index == self.selected_option else (255, 255, 255)
                text = self.font.render(option, 1, color)
                self.window.blit(text, (50, 50 + index * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_option] == "Back":
                            return 'back'
                        else:
                            # Placeholder for setting adjustment functionality
                            print(f"Adjusting {self.options[self.selected_option]}")

            return None