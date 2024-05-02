import pygame
import sys

class Losescreen:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("damn :(")

        
        self.font = pygame.font.SysFont("arial", 30)
    
    def draw_screen(self,gameword):
        self.screen.fill("white")
        self.images = pygame.transform.scale(pygame.image.load(f"assets/finalprojectimages/hangman{6}.png"), (350, 350))
        self.screen.blit(self.images,(225,0))
        
        lose_text = self.font.render(f"The word was: {gameword}", True, "black")
        lose_rect = lose_text.get_rect(center=(self.WIDTH/2, 25))
        self.screen.blit(lose_text, lose_rect)
        
        # win msg
        lose_text = self.font.render("Baxter's identity was revealed :(((((", True, "red")
        lose_rect = lose_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/4))
        self.screen.blit(lose_text, lose_rect)
        
        # Continue and exit buttons
        playagain_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT*3/4, 200, 50)
        exit_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT*3/4 + 70, 200, 50)
        
        pygame.draw.rect(self.screen, "black", playagain_button)
        pygame.draw.rect(self.screen, "black", exit_button)
        
        playagain_text = self.font.render("Play again?", True, "white")
        playagain_text_rect = playagain_text.get_rect(center=playagain_button.center)
        self.screen.blit(playagain_text, playagain_text_rect)
        
        exit_text = self.font.render("Exit", True, "white")
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        self.screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()

        return playagain_button, exit_button
    
    def run_screen(self, gameword):
        playagain_button, exit_button = self.draw_screen(gameword)

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if playagain_button.collidepoint(mouse_pos):
                        return True
                    elif exit_button.collidepoint(mouse_pos):
                        return False
                        

        
        