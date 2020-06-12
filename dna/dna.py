import sys
import csv

databaseFile = sys.argv[1]
sequenceFile = sys.argv[2]


# Open dna sequence
f = open(sequenceFile, "r")
DNA = f.read()

# Open .csv and read contents into memory
def main():
    with open(databaseFile) as csvfile:
        db = csv.DictReader(csvfile)
        match = "No match"
        for person in db:
            name = person['name']
            person.pop('name', None)
            if checkDNA(DNA, person):
                match = name
        print(match)

def checkDNA(s, personProfile):
    # Person is a dict with STR keys
    match = True
    for seq in personProfile:
        if int(personProfile[seq]) != countLongestSTR(s, seq):
            match = False
    return match


def countLongestSTR(s, substr):
    # Counts longest chain of strSEQ in dna sequence
    # The idea is to start a counter each time strSeq is encountered
    # Cut the substr or single letter off s to "move on"
    # Count the number of repetitions until s is ''
    counter = 0
    maxCount = 0
    inChain = False # Keep track of if the cut string comes off a repeat sequence
    while len(s) > 0:
        if s.startswith(substr):
            counter += 1
            inChain = True
            maxCount = max(maxCount, counter)
            s = s[len(substr):]
        else:
            maxCount = max(maxCount, counter)
            counter = 0
            inChain = False
            s = s[1:]
    return maxCount

main()