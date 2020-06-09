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

def getKeys(value):

    for key, item in alpha.items():
        if value.upper() == item:
            return key
    return False



def caesarEncrypt(plaintext, key):
    ciphertext = []
    for char in plaintext:
        charKey = getKeys(char)
        charKey = charKey + int(key) %26
        ciphertext.append(alpha[charKey])

    return ''.join(ciphertext)


def caesarDecrypt(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        charKey = getKeys(char)
        charKey = charKey - int(key) % 26
        plaintext.append(alpha[charKey])

    return ''.join(plaintext)

print("-------------------------------------------------------\nWelcome to the Encryption Playground!\nPlease choose fromt the following encryption schemes:\n")
print("[1] Caesar Cipher")

while True:
    choice = input("Please choose from the menu options: ")

    if choice == '1':
        
            plaintext = input("Please enter the plaintext you wish to encrypt: ")
            key = input("Please enter the key (1 - 25): ")
            
            cipher = caesarEncrypt(plaintext, key)
            print(cipher)
            choice = input("Would you like to decrpy the message? (Y or N) ")
            if choice.lower() == 'y':
                plaintext = caesarDecrypt(cipher, key)
                print(plaintext)
                
            
        

    elif choice.lower() == 'q':
        break
        
