import time
import binaryConv as binary

#This function takes two lists - the flip flop bits and the switch bits. Each call to this function acts as a single time step in the linear shift feedback loop.
#To create an 8 bit number, place the function call in a loop with 8 iterations
#The function implements the steps used by a Linear Shift Feedback Register used to generate psuedo-random numbers. Requires that the values to the flip flops and switches be pre-defined

def shiftFeedback (flip, switch):
    
    #The first(rightmost) flip flop value is the output for the current time step 
    output = flip[0] #Might be before or after the shift occurs?

    #First step is to shift the values of the flip flops over by 1
    for x in range(len(flip) - 1):
        flip[x] = flip[x+1]

    #After the shift, the value for the last flip flop must be generated. Done by XORing all values of the flip flops where the corresponding switch is equal to 1
    xorBits = []

    for y in range(len(switch)):
        if switch[y] == 1:
            #If the switch is equal to 1, the value in the flip flop and the switch are bitwise AND with the result placed into the xorBits list for later XORing
            xorBits.append(flip[y] & switch[y])
          
        
        

        #After each timestep, the value of the switches are changed depending on an AND 
        switch[y] ^= flip[y]
        
        
    
    #Figure out how to see if there are more than one 1s in the xorBits list. If more than 1 then the bit equals 0
    xorRes = 0
    #print(xorBits)
    for z in range(len(xorBits)):
        xorRes ^= xorBits[z]
    
    #Place the result of the Xor/And of the switches and flip flops into the leftmost flip flop.
    #print(flip)
    flip[len(flip) - 1] = xorRes  
    #print(flip)
    return output
        

#flipFlops = [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
#pSwitches = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1]


#randOutput = []
#count = 0
#numbers = []
#repeatFlag = 0


#for num in range(10000):
    
    #randNumber = []
    #count = count + 1
    
    #for _ in range(8):
        

        #rand = shiftFeedback(flipFlops, pSwitches)
        #randNumber.append(rand)
        
    #print(binary.unsignedDecimalEncode(randNumber))
    #numbers.append(binary.unsignedDecimalEncode(randNumber))

    
    #Finds the period cycle for the LSFR (How many timesteps until the output begins to repeat)
    #if count > 5 and numbers[num] == numbers[4]:# and numbers[num + 2] == numbers[6]:# and repeatFlag == 0:
        #print(numbers[4:])
        #print("Actual Repeat Found")
        #print("Cycle period: " + str(len(numbers[4:])))
        
        #repeatFlag = 1
  
