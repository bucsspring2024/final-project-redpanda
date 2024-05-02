import pygame
import sys

class Menu:

    def __init__(self):
        pygame.init()

        #screen
        self.WIDTH, self.HEIGHT = 800, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Hangman Binghaton University Edition")

        #font
        self.font = pygame.font.SysFont("Arial", 30)



    def draw_menu(self):
        self.screen.fill("white")

        #text
        text_surface = self.font.render("Help Baxter protect his identity with a game of hangman!", True, "Black")
        text_rect = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2 - 50))
        self.screen.blit(text_surface, text_rect)

        #buttons
        start_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT/2 + 50, 200, 50)
        quit_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT/2 + 150, 200, 50)

        pygame.draw.rect(self.screen, "dark green", start_button)
        pygame.draw.rect(self.screen, "Black", quit_button)

        start_text = self.font.render("Start", True, "white")
        start_text_rect = start_text.get_rect(center=start_button.center)
        self.screen.blit(start_text, start_text_rect)

        quit_text = self.font.render("Quit", True, "white")
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        self.screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

    def run_menu(self):
        while True:
            self.draw_menu()
            start_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT/2 + 50, 200, 50)
            quit_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT/2 + 150, 200, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button.collidepoint(mouse_pos):
                        return True
                        
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
    
    
