class HangmanWords:
    def __init__(self, gameword, guessed):
        self.gameword = gameword
        self.guessed = guessed

    def check_letter(self, letter):
        self.guessed.append(letter)
        if letter not in self.gameword:
            return False
        else:
            return True

    def all_letters_guessed(self):
        return all(letter in self.guessed for letter in self.gameword)
    
    
        