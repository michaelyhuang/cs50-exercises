import re
text = input("Text: ")

def main(t):
    nWords = countWords(t)
    nLetters = countLetters(t)
    L = nLetters/nWords * 100
    # print(L)
    # print(f'{nLetters} letter(s)')
    # print(f'{nWords} word(s)')

    nSentences = countSentences(text)
    S = nSentences/nWords * 100
    # print(S)
    # print(f'{nSentences} sentence(s)')
    
    index = 0.0588 * L - 0.296 * S - 15.8
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        grade = round(index)
        print(f'Grade {grade}')

def countSentences(s):
    # Counts the number of sentences in the string
    # Based on number of periods, exclamation points, question marks
    countPeriod = s.count(".")
    countExclam = s.count("!")
    countQuestion = s.count("?")
    return(countPeriod + countExclam + countQuestion)

def countLetters(s):
    # Counts the number of letters in the string
    # Any A-Z regardless of case
    pattern = '[a-z]'
    letterList = re.findall(pattern, s, flags=re.IGNORECASE)
    return(len(letterList))

def countWords(s):
    # Counts the number of words in the string
    wordList = re.findall(r'\S+', s)
    return(len(wordList))

main(text)