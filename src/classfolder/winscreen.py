import pygame
import sys

class WinScreen:
    def __init__(self):
        pygame.init()

        #screen
        self.WIDTH, self.HEIGHT = 800, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Congratulations!")
        
        #font
        self.font = pygame.font.SysFont("arial", 30)
    
        self.wins_in_row = 0

    def draw_screen(self,gameword,consecutivewins):
        self.screen.fill("white")
        
        #text1
        congrats_text = self.font.render("Congratulations, you won!", True, "black")
        congrats_rect = congrats_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/4))
        self.screen.blit(congrats_text, congrats_rect)

        #text2
        wins_text = self.font.render(f"The word was: {gameword}", True, "black")
        wins_rect = wins_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(wins_text, wins_rect)

        #buttons
        continue_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT*3/4, 200, 50)
        exit_button = pygame.Rect(self.WIDTH/2 - 100, self.HEIGHT*3/4 + 70, 200, 50)
        
        pygame.draw.rect(self.screen, "black", continue_button)
        pygame.draw.rect(self.screen, "black", exit_button)
        
        continue_text = self.font.render("Continue?", True, "white")
        continue_text_rect = continue_text.get_rect(center=continue_button.center)
        self.screen.blit(continue_text, continue_text_rect)
        
        exit_text = self.font.render("Exit", True, "white")
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        self.screen.blit(exit_text, exit_text_rect)
        
        wins_tally_text = self.font.render(f"wins in a row: {consecutivewins}", True, "black")
        wins_tally_rect = wins_tally_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/6))
        self.screen.blit(wins_tally_text, wins_tally_rect)

        pygame.display.flip()

        return continue_button, exit_button

    def run_screen(self, gameword, consecutivewins):
        continue_button, exit_button = self.draw_screen(gameword,consecutivewins)

        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if continue_button.collidepoint(mouse_pos):
                        self.wins_in_row += 1
                        return True
                    if exit_button.collidepoint(mouse_pos):
                        return False