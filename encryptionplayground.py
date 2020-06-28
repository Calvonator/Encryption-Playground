#This is the main file for the encryption playground where each encrytpion cipher is placed into its own file and imported here 
import caesar
import lsfr
import binaryConv as conv
import random

def generateSeed (flipFlops):
    ffseed = []
    switch = []
    for _ in range(int(flipFlops)):
        ffseed.append(random.randint(0, 1))
        switch.append(random.randint(0, 1))


    return ffseed, switch



print("-------------------------------------------------------\nWelcome to the Encryption Playground!\nPlease choose fromt the following encryption schemes:\n")
print("[1] Caesar Cipher")
print("[2] LSFR Psuedo-Random Number Generation or [21] to test period cycles of LSFR")



while True:
    choice = input("Please choose from the menu options: ")

    if choice == '1':
        
            plaintext = input("Please enter the plaintext you wish to encrypt: ")
            key = input("Please enter the key (1 - 25): ")
            
            cipher = caesar.encrypt(plaintext, key)
            print(cipher)
            choice = input("Would you like to decrpy the message? (Y or N) ")
            
            if choice.lower() == 'y':
                plaintext = caesar.decrypt(cipher, key)
                print(plaintext)
                
    elif choice == '2':
        
        ffSeed = []
        switch = []
        
        bitNumber = input("What bit size would you like the output to be? (8, 16, 32 and 64 bits)")

        switchChoice = input("Would you like to manually input the seed (Y) or automatically (N)?")

        if switchChoice.lower() == 'y':
            print("Please enter the values for the flip flop boxes individually: (0 or 1 or q)\n")
            
            while True:
                
                bit = input()
                
                if bit.lower() == '1' or bit.lower() == '0':
                    ffSeed.append(int(bit))
                else:
                    break
                
                

            randChoice = input("Would you like to input the switches manually (y) or randomly generate (n)?")
            
            if randChoice.lower() == 'y':
                noOfSwitches = len(ffSeed)
                print("Please enter the values for " + str(noOfSwitches) + " switches:\n")
                
                for _ in range(len(ffSeed)):

                    if noOfSwitches == 20 or noOfSwitches == 10 or noOfSwitches == 5 or noOfSwitches == 3 or noOfSwitches == 1:
                        print(str(noOfSwitches) + " more switches")
                    
                    bit = input()

                    if bit.lower() == '1' or bit.lower() == '0':               
                        switch.append(int(bit))

                    noOfSwitches = noOfSwitches - 1
                    
            elif randChoice.lower() == 'n':
                
                for _ in range(len(ffSeed)):
                    
                    switch.append(random.randint(0, 1))
                    
            
        
        elif switchChoice.lower() == 'n':
            noOfSwitches = input("What number of flip flop boxes would you like?")
            ffSeed, switch = generateSeed(int(noOfSwitches))
        
        numbers = []
            
        while True:
                
            randNumber = []
                
            for _ in range(int(bitNumber)):
                
                rand = lsfr.shiftFeedback(ffSeed, switch) 
                randNumber.append(rand)    
                    
            print(conv.unsignedDecimalEncode(randNumber))

            numbers.append(conv.unsignedDecimalEncode(randNumber)) 
            again = input("Generate another number?")

            if again.lower() == 'n':
                break
                
            print(numbers)

    elif choice == '21':
        ffSeed = []
        switch = []
        
        noOfSwitches = input("How many switches?")
        bitNumber = input("What bit size would you like the output to be? (8, 16, 32 and 64 bits)")

        ffSeed, switch = generateSeed(int(noOfSwitches))

        numbers = []
        count = 0

        for num in range(100000000):
            count += 1
            print(count)
            randNumber = []
            
            for _ in range(int(bitNumber)):
                randBit = lsfr.shiftFeedback(ffSeed, switch)
                randNumber.append(randBit)

            numbers.append(conv.unsignedDecimalEncode(randNumber))
            print(numbers)
      
            if count > 20 and numbers[num] == numbers[5]:
                #print(str(numbers[num]) + ' ' + str(numbers[20]))
                print(numbers[num])
                print("Repeat Found! Count: " + str(count))
                break


        




    elif choice.lower() == 'q':
        break
