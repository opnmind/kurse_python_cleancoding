import re
import random

def validateInput(inputnumber:int):
    """
    This Function validates UserInput
    """
    try:
        i = int(inputnumber)
        if i < 50:
            if i > 0:
                return i
            else: 
                print("Integer has to be between 1 and 49") 
        else: 
            print("Integer has to be between 1 and 49") 
    except ValueError:
        print("Please enter only integer! ") 

def generateRandomNumbers():
    """
    This Function generates 6 random numbers 
    """
    randlist:list = []
    for x in range(5):
        randlist.append(random.randint(1, 49))
    return randlist

def compareNumbers(inputNumbers: list, RandomNumbers: list):
    """
    This Function compares to list of numbers 
    """
    for y in inputNumbers:
        if y in RandomNumbers :
            print("Yes, you tipped " + y + "correctly!")



if __name__ == "__main__":
    mylist=[]
    for i in range(6):
        x = input("Number " + str(i+1) + ":")
        validatedInput = validateInput(i)
        mylist.append(validatedInput)
    compareNumbers(mylist, generateRandomNumbers())