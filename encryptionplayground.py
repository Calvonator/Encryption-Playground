#This is the main file for the encryption playground where each encrytpion cipher is placed into its own file and imported here 
import caesar

print("-------------------------------------------------------\nWelcome to the Encryption Playground!\nPlease choose fromt the following encryption schemes:\n")
print("[1] Caesar Cipher")

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
                
            
        

    elif choice.lower() == 'q':
        break
        
