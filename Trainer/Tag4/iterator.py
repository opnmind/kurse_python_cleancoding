class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration # Anmerkung, das ist nicht die einzig mögliche Reaktionsweise!


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)
# direkter: i = PowTo(3).__iter__(), mit eigener Methode angenehmer Aufrufbar, factory-Lösung wäre auhc interessant

# Using next to get to the next iterator element
print(next(i)) # next(i) -> return i.__next__()
print(next(i))
print(next(i))
print(next(i))
#print(next(i))

for n in PowTwo(4):
    print(n)