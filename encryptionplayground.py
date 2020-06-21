#This is the main file for the encryption playground where each encrytpion cipher is placed into its own file and imported here 
import caesar
import lsfr
import binaryConv as conv
import random

print("-------------------------------------------------------\nWelcome to the Encryption Playground!\nPlease choose fromt the following encryption schemes:\n")
print("[1] Caesar Cipher")
print("[2] LSFR Psuedo-Random Number Generation")



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
        
        print("Please enter the values for the flip flop boxes individually: (0 or 1 or q)\n")
        
        while True:
            
            bit = input()
            
            if bit.lower() == 'q':
                break
            
            ffSeed.append(int(bit))

        randChoice = input("Would you like to input the switches manually (y) or randomly generate (n)?")
        
        if randChoice.lower() == 'y':
            noOfSwitches = len(ffSeed)
            print("Please enter the values for " + str(noOfSwitches) + " switches:\n")
            
            for _ in range(len(ffSeed)):

                if noOfSwitches == 20 or noOfSwitches == 10 or noOfSwitches == 5 or noOfSwitches == 3 or noOfSwitches == 1:
                    print(str(noOfSwitches) + " more switches")
                
                bit = input()
                                
                switch.append(int(bit))

                noOfSwitches = noOfSwitches - 1
                
        elif randChoice.lower() == 'n':
            
            for x in range(len(ffSeed)):
                
                switch.append(random.randint(0, 1))
                
        numbers = []
        
        while True:
            
            randNumber = []
            
            for _ in range(8):
            
                rand = lsfr.shiftFeedback(ffSeed, switch) 
                randNumber.append(rand)    
                
            print(conv.unsignedDecimalEncode(randNumber))

            numbers.append(conv.unsignedDecimalEncode(randNumber)) 
            again = input("Generate another number?")

            if again.lower() == 'n':
                break
            
        print(numbers)
        
    elif choice.lower() == 'q':
        break
