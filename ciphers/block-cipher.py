

def sub(word):
    newWord = []
    subBox = {
        "a": "b",
        "b": "c",
        "c": "d",
        "d": "e",
        "e": "f",
        "f": "g",
        "g": "h",
        "h": "i",
        "i": "j",
        "j": "k",
        "k": "l",
        "l": "m",
        "m": "n",
        "n": "o",
        "o": "p",
        "p": "q",
        "q": "r",
        "r": "s",
        "s": "t",
        "t": "u",
        "u": "v",
        "v": "w",
        "w": "y",
        "y": "x",
        "x": "z",
        "z": "a"
        }
    for x in range(len(word)):
        newWord.append(subBox[word[x].lower()])
    
    return ''.join(newWord)

def subInverse(char):
    newWord = []
    subBox = {
        "a": "z",
        "b": "a",
        "c": "b",
        "d": "c",
        "e": "d",
        "f": "e",
        "g": "f",
        "h": "g",
        "i": "h",
        "j": "i",
        "k": "j",
        "l": "k",
        "m": "l",
        "n": "m",
        "o": "n",
        "p": "o",
        "q": "p",
        "r": "q",
        "s": "r",
        "t": "s",
        "u": "t",
        "v": "u",
        "w": "v",
        "y": "w",
        "x": "y",
        "z": "x"
        }
    
    for x in range(len(word)):
        newWord.append(subBox[word[x].lower()])
    
    return ''.join(newWord)




word = sub('helloh')
print(word)

word1 = subInverse(word)

print(word1)
