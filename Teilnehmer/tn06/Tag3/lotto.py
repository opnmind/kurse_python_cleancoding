"""
Modul Lotto

Dieses Modul simuliert ein Lottospiel
Hierbei kann der User via file 6 zahlen tippen
Diese werden auf ihre korrektheit geprüft (keine duplikate)
Desweiteren kann ein Spiel gestartet werden bei dem 6 zufällige Zahlen ermittelt werden
Diese werden mit den getippten Zahlen des Nutzers verglichen.
Bei übereinstimmung gewinnt der nutzer.

Ein Aufrufbeispiel

Verweise
"""
from random import randint

class LottoGame:
    '''
    Base Class for the Lotto Game
    '''
    def __init__(self):
        '''
        Class init for lottoGame
        Initialized Vars:
        - user_numbers
        - computer_numbers
        '''
        self.user_numbers = []
        self.computer_numbers = []

    def set_user_numbers(self, numbers):
        '''
        Setter method for usser_numbers
        '''
        self.user_numbers = numbers
    def get_user_numbers(self):
        '''
        Getter method for user_numbers
        '''
        return self.user_numbers
    def set_computer_numbers(self, numbers):
        '''
        Setter method for usser_numbers
        '''
        self.computer_numbers = numbers
    def get_computer_numbers(self):
        '''
        Getter method for user_numbers
        '''
        return self.computer_numbers

    def read_user_input(self, file_path):
        '''
        function to get the 6 user numbers
        the user numbers have to be in a file that is passed as argument
        '''
        user_file = open(file_path, "r")
        temp_numbers = user_file.read().splitlines()
        user_file.close()
        self.set_user_numbers(temp_numbers)

    def calculate_computer_numbers(self):
        '''
        function to generate random computer numbers
        '''
        temp_numbers = []
        for _ in range(6):
            value = randint(1, 49)
            print(value)
            temp_numbers.append(value)
        self.set_computer_numbers(temp_numbers)

    def compare_numbers(self):
        '''
        Function to compare user_numbers array with computer_numbers array
        in case they match it returns true, else false
        '''
        if (self.get_user_numbers == self.get_computer_numbers).all():
            return True
        else:
            return False

    def show_game_result(self):
        ''''
        Function to show message to user with the game result
        '''
        if self.show_game_result == True:
            print("Du hast gewonnen!")
        else:
            print("Leider verloren")

if __name__ == "__main__":
    # lies die nutzereingabe
    # zieh zahlen für den computer
    # vergleich computerzahlen mit nutzerzahlen und gib aus ob nutzer gewonnen hat
    mylotto = LottoGame()
    mylotto.read_user_input("/home/coder/Workspace/kurse_python_cleancoding/Teilnehmer/tn06/Tag3/my_tip.txt")
    mylotto.calculate_computer_numbers()
    mylotto.show_game_result()
