
#Converts 8, 16, 32 and 64 bit binary numbers into unsigned integers
def unsignedDecimalConv():
    bitBinary = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #Required for timeit testing

    
    bitExp = [9223372036854775808, 4611686018427387904, 2305843009213693952, 1152921504606846976, 576460752303423488, 288230376151711744, 144115188075855872, 72057594037927936, 36028797018963968, 18014398509481984, 9007199254740992, 4503599627370496, 2251799813685248, 1125899906842624, 562949953421312, 281474976710656, 140737488355328, 70368744177664, 35184372088832, 17592186044416, 8796093022208, 4398046511104, 2199023255552, 1099511627776, 549755813888, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    decimal = 0
    if len(bitBinary) == 8:
        bit = bitExp[-8:]
        
    elif len(bitBinary) == 16:
        bit = bitExp[-16:]

    elif len(bitBinary) == 32:
        bit = bitExp[-32:]

    elif len(bitBinary) == 64:
        bit = bitExp[-64:]

    else:
        print("Incorrect number of binary bit.\n" + str(len(binary)) + " bits given, require either 8, 16, 32 or 64 bit binary numbers")
    
    for x in range(len(bitBinary)):
        if bitBinary[x] == 1:
            
            decimal = decimal + bit[x]
    return decimal


def decimalConv():
    bitBinary = [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]  #Requires for timeit testing
    exp = [63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    decimal = 0
    
    if len(bitBinary) == 8:
        eightBitExp = exp[-8:]
        
        for x in range(8):
            if bitBinary[x] == 1:
                
                bit = 2**eightBitExp[x] 
                
                decimal = decimal + bit
        return decimal

    elif len(bitBinary) == 16:
        bitBinary = exp[-16:]
     
        for x in range(16):
            if bitBinary[x] == 1:
               
                bit = 2**bitBinary[x] 
               
                decimal = decimal + bit
        
        return decimal
    
    elif len(bitBinary) == 32:
        bitBinary = exp[-32:]
        
        for x in range(32):
            if bitBinary[x] == 1:
                
                bit = 2**bitBinary[x] 
                
                decimal = decimal + bit
    
        return decimal
    
    #bit = [128, 64, 32, 16, 8, 4, 2, 1]
    
    #decimal = 0





if __name__ == '__main__':
    import timeit
    
    print("unsignedDecimalConv(): " + str(timeit.timeit("unsignedDecimalConv()", setup="from __main__ import unsignedDecimalConv", number=1000000)) + " seconds")

    print("decimalConv(): " + str(timeit.timeit("decimalConv()", setup="from __main__ import decimalConv", number=1000000)) + " seconds")
