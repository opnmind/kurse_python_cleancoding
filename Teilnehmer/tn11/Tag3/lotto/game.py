
import random

class Lottery:


    _gussed_numbers = []
    _drawings = []


    def _validate_input(self, input_number):
        if not isinstance(input_number, int):
            raise TypeError("Only integers are allowed.")
        if input_number < 0 or input_number > 49:
            raise Exception("Numbers must be between 0 and 49")


    def get_gussed_numbers(self):
        return self._gussed_numbers.copy()


    def drawing(self):
        drawings = []
        while len(drawings) < 6:
            new_number = random.randint(0, 49)
            if new_number not in drawings:
                drawings.append(new_number)
        self._drawings = drawings
        return drawings.copy()


    def have_i_won(self):
        for i in self._drawings:
            if i not in self._gussed_numbers:
                return False
        return True


    def guess(self, *args):
        if len(args) != 6:
            raise Exception("Exactly 6 numbers must be used.")
        for i in args:
            self._validate_input(i)
            if i in self._gussed_numbers:
                raise Exception("Duplicated numbers are not allowed.")
            self._gussed_numbers.append(i)


if __name__ == "__main__":
    lottery = Lottery()
    lottery.guess(1, 2, 11, 4, 6, 9)
    print(lottery.get_gussed_numbers())
    print(lottery.drawing())
    print("Have I won?: ", lottery.have_i_won())