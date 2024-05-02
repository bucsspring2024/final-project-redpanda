import pygame
import math
import requests
import sys
from src.classfolder.menu import Menu
from src.classfolder.scenario import ScenarioMenu
from src.classfolder.winscreen import WinScreen
from src.classfolder.hangmanaudio import HangmanAudio
from src.classfolder.hangmanwords import HangmanWords
from src.classfolder.hangmanguy import HangmanGraphics
from src.classfolder.losescreen import Losescreen

class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #screen
        self.WIDTH, self.HEIGHT = 800, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Hangman Binghaton University Edition")
       
        #API 
        self.APIURL = "https://random-word-api.herokuapp.com/word"
        self.wordlength = 4
        
        #images
        self.images = [pygame.transform.scale(pygame.image.load(f"assets/finalprojectimages/hangman{i}.png"), (350, 350)) for i in range(7)]

        #font
        self.gamefont = pygame.font.SysFont("arial", 35)
        self.gamefonttwo = pygame.font.SysFont("arial", 20)

        #button 
        self.RADIUS = 20
        self.GAP = 15
        self.letters = []
        startx = round((self.WIDTH - (self.RADIUS * 2 + self.GAP) * 13) / 2)
        starty = 400
        lettera = 65
        for i in range(26):
            xcord = startx + self.GAP * 2 + (self.RADIUS * 2 + self.GAP) * (i % 13)
            ycord = starty + ((i // 13) * (self.GAP + self.RADIUS * 2))
            self.letters.append({"xcord": xcord, "ycord": ycord, "char": chr(lettera + i), "visible": True})

        #hanagman status
        self.losingnum = 6
        self.baxterform = 0
        self.gameword = self.apigetrandomword() 
        self.guessed = [] 
        
        #tally
        self.consecutive_wins = 0
        #get game items
        self.graphics = HangmanGraphics(self.screen, self.images, self.gamefont, self.gamefonttwo, self.letters, self.RADIUS, self.GAP)
        audiomusuc = 'assets/kawaii-kitsune-kevin-macleod-main-version-7984-04-02.mp3'
        effectmusic = 'assets/multi-pop-1-188165.mp3'
        self.audio = HangmanAudio(audiomusuc)
        self.effect = HangmanAudio(effectmusic)
        self.audio.play_music()
    
    def update(self):
        pass

    def draw(self):
        self.graphics.draw_game(self.baxterform)
        self.graphics.draw_buttons()
        self.graphics.draw_word(self.gameword, self.guessed)
    
    def apigetrandomword(self):
        feedback = requests.get(self.APIURL, params = {"number": 1, "length": self.wordlength})
        
        if feedback.status_code == 200:
            randomword = feedback.json()[0]
            randomword = randomword.upper()
            return randomword
        else: 
            print("api fail")
            exit()
        
                
    def gameloop(self):
        FPS = 60
        self.words = HangmanWords(self.gameword, self.guessed)
        gameclock = pygame.time.Clock()
        gameclock.tick(FPS)
        print("the word is",self.gameword)
        self.handle_events()
        self.update()
        self.draw()
        pygame.display.update()
                
    def restartgame(self):
        self.baxterform = 0
        self.guessed.clear()
        self.gameword = self.apigetrandomword() 
        for letter in self.letters:
            letter["visible"] = True

        self.mainloop()

        
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.effect.play_effect()
                self.handle_mouse_click(pygame.mouse.get_pos())

    def handle_mouse_click(self, pos):
        mousex, mousey = pos
        for letter in self.letters:
            xcord, ycord, char, visible = letter.values()
            if visible:
                dis = math.sqrt((xcord - mousex) ** 2 + (ycord - mousey) ** 2)
                if dis < self.RADIUS:
                    letter["visible"] = False
                    if not self.words.check_letter(char):
                        self.baxterform += 1
                        if self.baxterform == self.losingnum:
                            menu = Losescreen()
                            if menu.run_screen(self.gameword):
                                self.consecutive_wins = 0
                                self.restartgame() 
                                return False
                            else:
                                pygame.quit()
                                sys.exit()
                    
                    elif self.words.all_letters_guessed():
                        menu = WinScreen()
                        self.consecutive_wins += 1
                        if menu.run_screen(self.gameword,self.consecutive_wins):
                            self.restartgame() 
                            return True
                        else:
                            pygame.quit()
                            sys.exit()
                            
                                
                                

    def mainloop(self):
        menu= Menu()
        scenario = ScenarioMenu()
        if menu.run_menu():
            if scenario.run_menu():
                while True:
                    self.gameloop()    