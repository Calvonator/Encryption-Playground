def shiftFeedback (flip, switch):
    output = flip[0] #Might be before or after the shift occurs
    #print(flip)
    for x in range(len(flip) - 1):
        flip[x] = flip[x+1]
    
    #print(flip)
    xorBits = []
    for y in range(len(switch) - 1):
        if switch[y] == 1:
            xorBits.append(flip[y])
        
        #print("Switches Before: " + str(switch))
        #print(str(switch[y]) + str(flip[y]))
        

        #P Switch XOR 
        switch[y] = switch[y] ^ flip[y]
        #if switch[y] == 1 and flip[y] == 1:
            #switch[y] = 1
        #else:
            #switch[y] = 0
         
        #print("Switches After: " + str(switch))
        
    #Figure out how to see if there are more than one 1s in the xorBits list. If more than 1 then the bit equals 0
        
    
    return output

#Takes an 8 bit binary as a list and coverts it to decimal (Create a modules for all binary conversions(8, 16, 32 and 64 bits))
def eightBitDecimalConv(bitBinary):

    if len(bitBinary) != 8:
        print("Binary input is not an 8-bit binary number")
        return False
    
    bit = [128, 64, 32, 16, 8, 4, 2, 1]
    decimal = 0
    for x in range(len(bitBinary)):
        if bitBinary[x] == 1:
            decimal = decimal + bit[x]
    return decimal

        

flipFlops = [0, 0, 0, 1]


pSwitches = [1, 1, 1, 1]

randOutput = []

for _ in range(8):
    outputBit = shiftFeedback(flipFlops, pSwitches)
    randOutput.append(outputBit)

print("Random Output")
print(randOutput)


print(flipFlops)

binary = [1, 0, 0, 0, 0, 0, 1, 1]

print("Random Decimal")
print(eightBitDecimalConv(randOutput))
