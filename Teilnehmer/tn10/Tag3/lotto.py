

class Lotto():
    """ Lotto """"

    def _stdinhandler(self):
        tipps = []
        for line in sys.stdin:
            int_tipp=self.verify(line)
            tipps.append(int_tipp)
        return tipps

    def _filehandler(self, path):
        topps = []
        with open(path) as file:
            for line in file:
                int_tipp=self.verify(line)
                tipps.append(int_tipp)
        return tipps

    def get_tipps(self, input_handler = _stdinhandler) 
        self.tipps = input_handler
        return self 

    def get_tip(self, draw):
        if len(draw) != 6:
            raise Exception
        self.draw = draw.sort() 

    def get_draw(self):
        numbers = range(1,50)
        random.shuffle(numbers)
        draw_numbers = numbers[:6]
        return draw_numbers.sort()

    def compare(self):
        pass 

    def export_result(self):
        pass  

if __name__ == "__main__":
    lotto = Lotto()
    


