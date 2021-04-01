

class Lotto:
    """Lotto Klasse"""

    TIPFILE = "/home/coder/Workspace/kurse_python_cleancoding/Teilnehmer/tn08/Tag3/lotto_tip.txt"

    def __init__(self, tip_file = None):
        self.tip_file = tip_file if tip_file else self.TIPFILE
        self.my_tip = []
        self.drawing_tip = []

    def enter_tip(self):
        with open(self.tip_file) as file_descriptor:
            for line in file_descriptor:
                tip = int(line)
                self.my_tip.append(tip)
        return self

    def check_tip(self):
        print(len(self.my_tip))
        print(self.my_tip)
        assert len(self.my_tip) == 6
        assert all(isinstance(n, int) for n in self.my_tip)
        return self


    def generate_drawing(self):
        pass

    def compare_tip_to_drawing(self):
        pass

    def show_result(self):
        return 



if __name__ == "__main__":
    print(Lotto().enter_tip().check_tip())
