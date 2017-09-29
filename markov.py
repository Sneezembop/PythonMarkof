
from itertools import tee, islice, chain, izip
import random


def previous_and_prevPrevious(some_iterable):
    pprevs, prevs, items = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    pprevs = chain([None], [None], pprevs)
    return izip(pprevs, prevs, items)

def toString(text):
    if (text == None):
        return "";

    return text;


def buildDict(text):

    mydict = {}

    words = text.split(" ")

    for pprev, prev, item,in previous_and_prevPrevious(words):
        #print "pp:", pprev, "p:", prev, "i:", item

        pref = toString(pprev) + " " + toString(prev)
        suff = toString(item)

        if (pref in mydict):
            mydict[pref].append(suff)
        else:
            mydict[pref] = [suff]
    
    return mydict;

def buildMarkov(dictionary, length):

    output = ""
    curPref = " "
    lastSuf = ""

    while (length > 0):
        temp = ""

        dictionary[curPref]

        secure_random = random.SystemRandom()
        temp = secure_random.choice(dictionary[curPref])

        output += " " + temp

        curPref = lastSuf +" "+ temp
        lastSuf = temp

        length -= 1

    return output

def main():
    myfile = open("input.txt", "r")

    mydict = buildDict(myfile.read())

    #print(mydict)
    outputFile = open("output.txt", "w")

    outputFile.write(buildMarkov(mydict, 1000))

main()