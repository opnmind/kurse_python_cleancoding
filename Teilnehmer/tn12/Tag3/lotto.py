#!/usr/bin/env python3
from random import randint
in49 = []
in49shuffing = []
 
def lotto():
    """ Lets play Lotto """
    print("Bitte 6 zahlen zwischen 1 und 49 wählen: ")
    z1,z2,z3,z4,z5,z6 = 0,0,0,0,0,0
 
    # fill variable
    for i in z1,z2,z3,z4,z5,z6:
        i = input()
        i = int(i)
        if i <1 or i >49:
            validIn(i)
        elif i in in49:
            alreadyIn(i)
        else:
            in49.append(i)
 
    in49.sort()
    print("Ihre Eingabe ist: ",in49)
    print("Lottozahlen werden gewürfelt, bitte warten ...")
 
    # play Lotto
    roundAll, round5, round4 = 0,0,0
    while in49 != in49shuffing:
        del in49shuffing[:]
        lottoDigits()
        in49shuffing.sort()
         
        counter = 0
        for i in range(0,6):
            if in49shuffing[i] in in49:
                counter += 1
        if counter == 4:
            round4 += 1
        if counter == 5:
            round5 += 1
 
        roundAll += 1
 
    # print result
    print ("Lottozahlen: ", in49shuffing, "in der",roundAll, "Runde")
    print ("Die Wahrscheinlichkeit auf einen 6er im Lotto betrug: ", 100/roundAll, "%" )
    print ("Die Wahrscheinlichkeit auf einen 5er im Lotto betrug: ", round5 * 100/roundAll, "%" )
    print ("Die Wahrscheinlichkeit auf einen 4er im Lotto betrug: ", round4 * 100/roundAll, "%" )
 
def alreadyIn(elem):
    """ check if number already in list"""
    print("Die Eingabe",elem," wurde schon ausgewählt. Neuer Versuch: ")
    elem = input()
    elem = int(elem)
    if elem < 0 or elem > 49:
        validIn(elem)
    else:
        in49.append(elem)
 
def validIn(elem):
    """ check if number is valid in range 1 to 49 """
    print ("Die Eingabe",elem," ist ungültig. Neuer Versuch: ")
    elem = input()
    elem = int(elem)
    if elem in in49:
        alreadyIn(elem)
    else:
        in49.append(elem)
 
def lottoDigits():
    """ generate a list with 6 int between 1 and 49 """
    while len(in49shuffing) != 6:
        lZ = randint(1,49)
        if lZ not in in49shuffing:
            in49shuffing.append(lZ)
    in49shuffing.sort()
 
def main():
    lotto()
 
if __name__ == "__main__":
    main()