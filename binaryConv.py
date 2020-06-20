
#Converts 8, 16, 32 and 64 bit binary numbers into unsigned integers
def unsignedDecimalEncode(binary):
    bitBinary = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #if len(bitBinary) != 8:
        #print("Binary input is not an 8-bit binary number")
        #return False
    
    bitExp = [9223372036854775808, 4611686018427387904, 2305843009213693952, 1152921504606846976, 576460752303423488, 288230376151711744, 144115188075855872, 72057594037927936, 36028797018963968, 18014398509481984, 9007199254740992, 4503599627370496, 2251799813685248, 1125899906842624, 562949953421312, 281474976710656, 140737488355328, 70368744177664, 35184372088832, 17592186044416, 8796093022208, 4398046511104, 2199023255552, 1099511627776, 549755813888, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    decimal = 0
    if len(binary) == 8:
        bit = bitExp[-8:]
        
    elif len(binary) == 16:
        bit = bitExp[-16:]

    elif len(binary) == 32:
        bit = bitExp[-32:]

    elif len(binary) == 64:
        bit = bitExp[-64:]

    else:
        print("Incorrect number of binary bit.\n" + str(len(binary)) + " bits given, require either 8, 16, 32 or 64 bit binary numbers")
    
    for x in range(len(binary)):
        if binary[x] == 1:
            #print(bit[x])
            decimal = decimal + bit[x]
    return decimal

#Converts a 16 bit decimal value to a 16 bit binary string
def unsigned16BitDecimalDecode(decimal):

    binary = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    if decimal > 2**16:
        print("Unsigned decimal is greater than 16 bits")
        return False

    if decimal > 2**15:
        binary[0] = '1'
        decimal = decimal - 2**15
        
    if decimal > 2**14:
        binary[1] = '1'
        decimal = decimal - 2**14
    
    if decimal > 2**13:
        binary[2] = '1'
        decimal = decimal - 2**13

    if decimal > 2**12:
        binary[3] = '1'
        decimal = decimal - 2**12

    if decimal > 2**11:
        binary[4] = '1'
        decimal = decimal - 2**11

    if decimal > 2**10:
        binary[5] = '1'
        decimal = decimal - 2**10

    if decimal > 2**9:
        binary[6] = '1'
        decimal = decimal - 2**9

    if decimal > 2**8:
        binary[7] = '1'
        decimal = decimal - 2**8

    if decimal > 2**7:
        binary[8] = '1'
        decimal = decimal - 2**7

    if decimal > 2**6:
        binary[9] = '1'
        decimal = decimal - 2**6

    if decimal > 2**5:
        binary[10] = '1'
        decimal = decimal - 2**5

    if decimal > 2**4:
        binary[11] = '1'
        decimal = decimal - 2**4

    if decimal > 2**3:
        binary[12] = '1'
        decimal = decimal - 2**3

    if decimal > 2**2:
        binary[13] = '1'
        decimal = decimal - 2**2

    if decimal > 2**1:
        binary[14] = '1'
        decimal = decimal - 2**1

    if decimal == 1:
        binary[15] = '1'

    elif decimal == 0:
        binary[15] = '0'
        
    return ''.join(binary)
