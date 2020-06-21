# Encryption-Playground

This is an area for me to learn how to implement different cipher encryptions. 

# Table of Contents
<a href="#ciphers">Ciphers</a>
<br>
<a href="#random-number-generation">Random Number Generation</a>
<br>
<a href="#binary-conversion">Binary Conversion</a>


## Ciphers

### Caesar Cipher

A basic cipher that takes a plaintext and key (1-26), and produces a ciphertext by substituting each character with the character that is the value of the key places ahead within the alphabet. 

**To-Do**
- Modify the cipher so that non-alphabetical character can be encrypted.
- Create a form of the cipher that converts the plaintext to binary and then performs a bitshift (key value) to encrypt/decrpyt

### Block Cipher 

A cipher that encrypts a block at a time. Currently still need to make it work - currently only permutation/inverse permutation is setup.

**To-Do**
- Create a diagram of the process as a guidline for rest of the development.


## Random Number Generation

### Linear Shift Feedback Register
A linear shift feedback register (LSFR) of *n* period has *n* Flip Flops and *n* switches that contain 1 bit each. These bits are pre-determined and known as the seed. LSFR's are psuedo-random and begin to repeat, known as the period cycle. The maximum length of this period is 2^*n* - 1. 

**To-Do**
- Find the best combination of Flip Flop and Switch seeds. Try reach a period length of over 1000
- Try and attack the random number generation (Solving a system of linear equations).
- Figure out how to combine multiple LSFRs to create a stronger generation of random numbers
- In that case that the user chooses to manually enter switch values, find the length of the flip flop bits entered, present this number and enter a forced loop for that many iterations. 


## Binary Conversion

### binaryConv.py

This file is for functions that will encode/decode data representations to and from binary. Currently has the following functions:

**unsignedDecimalEncode**

Takes a binary input of 8, 16, 32 or 64 bits and encodes it as an unsigned decimal (integer)

**To-Do**
- Figure out how to use map() and lambda to perform the for loop that generates the decimal value.

**unsigned16BitDecimalDecode**

Takes a 16 bit (no greater than 2^16) decimal (integer) and decodes the value to a 16 bit binary string.

**To-Do**
- Modify the function to ask what number of bits the user would like the binary output to be and/or just use a 64/128 bit base binary and use padding
- Figure out a more efficient way of converting the decimal to binary (Test if a loop/map()/lambda is quicker than the series of if statements)


### conversiontesting.py

This file was used to test the time difference between two functions that both converted binary to decimal. The **unsignDecimalConv** function uses a list that has the values of 2^0-63 placed in a list used to lookup the value of a particular bit, while **decimalConv** performs the exponential operation at run-time.

The results of this timeit test shows the function that performs the exponential operation at runtime (**decimalConv**) is 46 percent faster:
```
unsignedDecimalConv(): 5.4829409 seconds
decimalConv(): 2.9273619 seconds
```

**To-Do**
- Do some more testing of with this file (Different Decode methods).



