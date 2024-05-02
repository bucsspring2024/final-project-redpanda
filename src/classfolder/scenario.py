import pygame
import random
import sys

class ScenarioMenu:

    def __init__(self):
        pygame.init()
        
        #screen
        self.WIDTH, self.HEIGHT = 800, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Scenario Menu")
        
        #font
        self.font = pygame.font.SysFont("arial", 15)
        
        self.scenarios = [
            "Scenario 1: Baxter wakes up to find that he is late for his 8am final exam!!!! the horror!!",
            "Scenario 2: Baxter wants to attend spring fling. Good for him. Let's help him",
            "Scenario 3: Baxter sees a dog",
            "Scenario 4: Baxter ended up in space????? let's help him get down",
            "Scenario 5: Baxter is in CS110",
            "Scenario 6: Baxter goes to cheese club",
            "Scenario 7: Baxter got lost in fine arts",
            "Scenario 8: Baxter is breakdancing on the spine????????",
            "Scenario 9: Baxter is attending to his mascot duties",
            "Scenario 10: Baxter is graduating",
        ]
        self.backgrounds = [
            "assets/scenario1image.jpg",
            "assets/scenario2image.jpg",
            "assets/scenario3image.jpg",
            "assets/scenario4image.jpg",
            "assets/scenario5image.jpg",
            "assets/scenario6image.jpg",
            "assets/scenario7image.jpg",
            "assets/scenario8image.jpg",
            "assets/scenario9image.jpg",
            "assets/scenario10image.jpg",
        ]
        
        self.current_scenario, self.current_background = self.generate_scenario()

        #button
        self.continue_button = pygame.Rect(self.WIDTH/2 - 50, self.HEIGHT - 100, 100, 50)

     
       

    def generate_scenario(self):
        randnum = random.randint(0, 9)
        return self.scenarios[randnum], self.backgrounds[randnum]

    def draw_menu(self):
        self.screen.fill("white")
        
        #background image
        background = pygame.image.load(self.current_background)
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))  # Resize image to fit screen
        self.screen.blit(background, (0, 0))
        
        #scenario
        text_rect = pygame.Rect(50, self.HEIGHT/2 - 50, self.WIDTH - 100, 100)  # Adjusted dimensions for the white rectangle
        pygame.draw.rect(self.screen, "white", text_rect)
        text_surface = self.font.render(self.current_scenario, True, "black")
        text_rect = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(text_surface, text_rect)
       
        
        #button
        pygame.draw.rect(self.screen, "black", self.continue_button)
        continue_text = self.font.render("Continue", True, "white")
        continue_text_rect = continue_text.get_rect(center=self.continue_button.center)
        self.screen.blit(continue_text, continue_text_rect)
        
        pygame.display.flip()

    def run_menu(self):
        while True:
            self.draw_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.continue_button.collidepoint(mouse_pos):
                        return True, self.current_scenario
                        