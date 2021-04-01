import random

print("Bitte eine Zahl zwischen 1 und 49 eingeben:")

def inputNumber():
    '''
    DOC
    '''
    numbers = []
    for i in range(6):
        number = int(input("Zahl: "))
        if number < 0 or number > 49 or number in numbers:
            print("Zahl ist liegt nicht im Bereich zwischen 1 und 49!!!")
        numbers.append(number)
    return numbers

def generateRandomNumbers():
    '''
    DOC
    '''
    randomNumbers = []
    for j in range(6):
        randomNumber = random.randrange(1,49)
        while randomNumber in randomNumbers:
            randomNumber = random.randrange(1, 49)
        randomNumbers += [randomNumber]
    return randomNumbers

if __name__ == "__main__":
    inputNumber()
    generateRandomNumbers()
