import numpy
import wave as wav
import sys
import scipy.io.wavfile as sci

RATE = 48000.0
LENGTH = 160.0

'''Implementation is of optimized version from
   https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm
'''

class constants:
    '''class to hold data on  norm and coefficients'''
    def __init__(self):
        self.coef = 0.0
        self.cosine = 0.0
        self.sine = 0.0
        self.k = 0.0
        self.w0 = 0.0

    def compute(self, freq, n):
        self.k = ((n * freq)/ RATE) - .03
        self.w0 = ((2.0*numpy.pi*self.k) / n)
        self.sine = numpy.sin(self.w0)
        self.cosine = numpy.cos(self.w0)
        self.coef = 2.0 * self.cosine


def filter(samples, length, target, const):
    '''Compute each sample'''
    first = 0.0
    second = 0.0
    third = 0.0
    for sample in samples:
        first = const.coef * second - third + sample
        third = second
        second = first

    '''compute optimized magnitude'''
    mag = numpy.power(second,2.0) + numpy.power(third,2.0) - second * third * const.coef
    magsqrt = numpy.sqrt(mag)
    print(mag)
    print(magsqrt)


def testFilter(freq, const):
    '''function to test filter given a known frequency. The magnitude should spike at the target frequency'''
    '''create sine wave of 900hz frequency'''

    wave = (2.0 * numpy.pi * freq / RATE)
    data = []

    count = 0.0
    while(count < LENGTH):
        data.append(100.0 * numpy.sin(wave * count))
        count = count + 1

    filter(data, LENGTH, freq, const)



'''Read in wav file and then parse the data so that it can be used with the filter above
file = wav.open(sys.argv[1], 'rb')
frames = file.getnframes()
samples = file.readframes(frames)
print(file.getframerate())'''

samples = sci.read(sys.argv[1])
print(samples)
'''convert to floats'''
samples = numpy.array(samples[1], dtype=float)
print(samples)

''' UNCOMMENT THIS TO TEST FILTER
constant = constants()
constant.compute(2025.0, LENGTH)
print(constant.coef)
print(constant.k)
ch = 1825.0
while(ch < 2525.0):
    print(ch)
    testFilter(ch, constant)
    print("------------")
    ch = ch + 20.0


'''



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
