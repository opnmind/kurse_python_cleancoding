import sys

class Lotto():
    """
    lottoklasse
    """

    def __init__(self):
        """
        inits the lotto class
        """
        pass

    def _stdinhandler(self): 
        tipps = []
        for line in sys.stdin:
            int_tipp = self.verify(line)
            tipps.append(int_tipp)
            print(tipps)
        return tipps

    def _fileinhandler(self, path):
        tipps = []
        with open(path) as file:
            for line in file:
                tipps.append(line)
       
        return tipps


    def read_tipps(self, input_handler=_stdinhandler):
        self.tipps = input_handler
        return self

    
    def verify(self, tipps=None):
        if not tipps:
            tips = self.tipps
        for tipp in tips:
            try:
                int_tipp = int(float(tipp))
            except Exception as e:
                raise e
                     

if __name__ == "__main__":
    lotto = Lotto()
    lotto.read_tipps(lotto._stdinhandler())
    for tip in lotto.tipps:
        print(type(tip))