import numpy

def filter(samples, length, frequency, rate):



'''
160 samples per bit
300 bits
37.5 bytes

length is equal to N in the article ? I think
returns two things? freqs and results

Should use the optimized filter that was in the embedded article it is easier and faster.

when the filter is run you get the maginitude back. That magnitude shoud spike at the target frequency
all other values should form a bell shaped curve. 
FIgure out the constants. Target frequency, block size, length, and so on. 
'''
