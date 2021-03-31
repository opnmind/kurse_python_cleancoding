"""Doscstring"""
import random

class TooBigNumberError(Exception):
    pass

class Game:
    """Doscstring"""

    def __init__(self):
        """Doscstring"""
        self._tipp = []
        self._ziehung = []
        self._matches = 0

    def load_tipp(self, reader, split_symbol=","):
        """Doscstring"""
        tipp = reader.read().split(split_symbol)
        if len(tipp) != 6:
            raise IndexError("Falsche Anzahl")
        tipp = [int(n) for n in tipp]
        for n in tipp:
            if n < 1 or n > 49:
                raise TooBigNumberError()
        if len(set(tipp)) != 6:
            raise ValueError("Doppelter Wert")
        self._tipp = tipp
        return self

    def roll_dices(self):
        """Doscstring"""
        self._ziehung = random.sample(range(1, 50), 6)
        return self

    def count_matches(self):
        """Doscstring"""
        self._matches = len(set(self._ziehung).intersection(set(self._tipp)))
        return self

    def send_results(self, writer, formatter=None):
        """Doscstring"""
        if formatter:
            text = formatter(self._tipp, self._ziehung, self._matches)
        else:
            text = f"{self._tipp} {self._ziehung} {self._matches}"
        writer.send(text)
        return self
