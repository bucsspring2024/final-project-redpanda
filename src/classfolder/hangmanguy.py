import pygame

class HangmanGraphics:
    def __init__(self, screen, images, gamefont, gamefonttwo, letters, RADIUS, GAP):
        self.screen = screen
        self.images = images
        self.gamefont = gamefont
        self.gamefonttwo = gamefonttwo
        self.letters = letters
        self.RADIUS = RADIUS
        self.GAP = GAP

    def draw_game(self, baxterform):
        self.screen.fill("white")
        self.screen.blit(self.images[baxterform], (0, 0))
        
    def draw_buttons(self):
        for letter in self.letters:
            xcord, ycord, char, visible = letter["xcord"], letter["ycord"], letter["char"], letter["visible"]
            if visible:
                pygame.draw.circle(self.screen, "dark green", (xcord, ycord), self.RADIUS, 0)
                text = self.gamefont.render(char, 1, "white")
                textxcenterer = text.get_width() / 2
                textycenterer = text.get_height() / 2
                self.screen.blit(text, (xcord - textxcenterer, ycord - textycenterer))
        
    def draw_word(self, gameword, guessed):
        dysplayword = ""
        for letter in gameword:
            if letter in guessed:
                dysplayword += letter + " "
            else:
                dysplayword += "_ "
        text = self.gamefonttwo.render(dysplayword, 1, "black")
        self.screen.blit(text, (400, 200))
    