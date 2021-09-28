from os import system
import random
from character import Character

class Game:
    """the controller of interface"""

    attempts:int
    complete:int
    placeholder:list
    target:list
    difficulty:int
    words = {"easy":[], "medium": [], "hard": []}
    run:bool
    given_words:list

    def __init__(self):
        self.interface = Character()
        self.set_data()

    def set_data(self) -> None:
        """brings the words from given file"""

        with open("data.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "")

                if len(line) > 6:
                    self.words["hard"].append(line)
                elif len(line) > 5:
                    self.words["medium"].append(line)
                else:
                    self.words["easy"].append(line)

    def play(self) -> None:
        """start the game, and the end have the posibility of restart the game"""

        choice = "y"
        while choice != "n":
            
            if choice == "y":
            
                self.config()
                while self.run:
                    self.run = self.attempt()

                if self.complete >= len(self.target):
                    print(f"You win, the word was {self.target}")
                else:
                    print(f"You lose, the word was {self.target}")

            self.interface.reset_state()
            choice = input("Do you want to play again?\n-> y = continue\n-> n = stop\n")

        print("End of program")

    def config(self) -> None:
        """initial configuration of game"""

        self.run = True
        self.complete = 0
        self.placeholder = []
        self.given_words = []

        can_use = False
        while not can_use:
            selection = input("Choose difficulty\n 1 = Easy\n 2 = Medium\n 3 = Hard\n")

            if selection.isnumeric():
                can_use = True
                selection = int(selection)
                self.target = self.select_word(selection)
                self.difficulty = selection
                self.set_difficulty()

                i = 0
                while i < len(self.target):
                    self.placeholder.append("_")
                    i += 1

    def attempt(self) -> bool:
        """each word into the system, runnning the game"""

        if self.attempts >= 0:

            if self.complete < len(self.target):

                system("cls")
                print(f"You have {self.attempts} attempts left, write ONE word and count tildes")
                print("You have tried: ", " ".join(self.given_words))
                self.interface.show_ui()
                print("Your progress: ", " ".join(self.placeholder))
                well = False
                choosen = input("Your word: ")

                for i in range(len(self.target)):
                    if choosen == self.target[i]:

                        if self.placeholder[i] != self.target[i]:
                            well = True
                            self.placeholder[i] = choosen
                            self.complete += 1
                
                if not well:
                    self.attempts -= 1
                    self.interface.define_state(self.attempts)
                    self.given_words.append(choosen)
                
                return True
            else:
                return False
        else:
            return False

    def select_word(self, dif) -> str:
        """returns a string with the selected word"""

        if dif == 1:
            level = self.words["easy"]
        elif dif == 2:
            level = self.words["medium"]
        elif dif == 3:
            level = self.words["hard"]
        else:
            return False

        index = random.randint(0, len(level) - 1)
        word = level[index]
        return word

    def set_difficulty(self) -> None:
        """define the allowed attempts"""

        if self.difficulty == 1:
            self.attempts = 5
        elif self.difficulty == 2:
            self.attempts = 3
        elif self.difficulty == 3:
            self.attempts = 1
        else:
            self.attempts = 3