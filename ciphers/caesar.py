#This python file contains the funcitons required to perform a caesar cipher encryption and decryption
alpha = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "Y",
    24: "X",
    25: "Z"     
    }

#Given a value, it finds the key for the value within the alpha dictionary
def getKeys(value):

    for key, item in alpha.items():
        if value.upper() == item:
            return key
    return False


#Given a plaintext and a key (int between 1-25), returns a ciphertext that is encrypted using Caesar cipher
def encrypt(plaintext, key):
    ciphertext = []
    for char in plaintext:
        charKey = getKeys(char)
        charKey = charKey + int(key) %26
        ciphertext.append(alpha[charKey])

    return ''.join(ciphertext)

#Given a plaintext and the same key it was encrypted with (int between 1-25), returns a plaintext that is encrypted using Caesar cipher
def decrypt(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        charKey = getKeys(char)
        charKey = charKey - int(key) % 26
        plaintext.append(alpha[charKey])

    return ''.join(plaintext)
