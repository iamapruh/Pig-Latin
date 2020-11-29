from changeColors import color

EXCEPTIONS = {
    "honest":"honestyay",
}

def convertToPigLatin(sentence):
    #Format the the sentence
    original = sentence.strip().lower()

    # split sentence into words
    words = original.split()

    # loop through words and convert to pig latin
    newWords = []

    for word in words:
        if word in EXCEPTIONS:newWords.append(EXCEPTIONS[word])
        # if word starting with vowel
        elif word[0] in "aeiou":
            if word[-1] != "y":newWord = word + "yay"
            else:newWord = word + "ay"
            newWords.append(newWord)
        # if word not starting with a vowel
        else:
            #Get the first vowel position
            vowelPos = 0
            for letter in word:
                if letter not in "aeiou":
                    vowelPos = vowelPos + 1
                else:
                    break

            #Convert it from there
            cons = word[:vowelPos]
            theRest = word[vowelPos:]
            new_word = theRest + cons + "ay"
            newWords.append(new_word)
                    
    # stick words back together
    output = " ".join(newWords) 
    
    return output

def tests():
    testCase1 = {
        "pig": ["igpay"],
        "latin": ["atinlay"],
        "banana" : ["ananabay"],
        "will" : ["illway"],
        "butler" : ["utlerbay"],
        "happy" : ["appyhay"],
        "duck" : ["uckday"],
        "me" : ["emay"],
        "bagel" : ["agelbay"]
    }
    testCase2 = {
        "smile" : ["ilesmay"],
        "string" : ["ingstray"],
        "stupid" : ["upidstay"],
        "glove" : ["oveglay"],
        "trash" : ["ashtray"],
        "floor": ["oorflay"],
        "store": ["orestay"],
    }

    testCase3 = {
        "eat" : ["eatyay", "eatay"],
        "omelet" : ["omeletyay", "omeletay"],
        "are" : ["areyay", "areay"],
        "egg" : ["eggyay", "eggay"],
        "explain" : ["explainyay"],
        "always" : ["alwaysyay", "alwaysay"],
        "ends" : ["endsyay", "endsay"],
        "honest" : ["honestyay"],
        "i": ["iyay"],
    }

    testCases = [testCase1, testCase2, testCase3]
    for testCase in testCases:
        for test, output in testCase.items():
            try:
                outputGiven = convertToPigLatin(test) 
                output.index(outputGiven)
            except Exception:
                raise AssertionError(f"""
                    --- Test Case Failed! ----
                    Test Case : {test}
                    Valid Outputs : {output}
                    Got Output : {outputGiven}
            
            """)

tests()

if __name__ == "__main__":
    print("\n")
    print(color(convertToPigLatin("This project was made by Navdeep Kante"), "cyan"))
    print(color("To quit, press enter without giving any sentence\n", "red"))
    while True:
        sentence = input(color("    Enter sentence to convert : ", "green"))
        if not sentence or len(sentence) == 0:break
        convertedSentence = color(convertToPigLatin(sentence), 'yellow')
        print(f"    {convertedSentence}\n")
    
