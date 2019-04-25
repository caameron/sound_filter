import numpy

RATE = 8000

'''Implementation is of optimized version from
   https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm
'''

class constants:
    '''class to hold data on  norm and coefficients'''
    def __init__(self):
        self.coef = 0
        self.cosine = 0
        self.sine = 0
        self.k = 0
        self.w0 = 0

    def compute(self, freq, n):
        self.k = ((n * freq)/ RATE)
        self.w0 = ((2*numpy.pi*self.k) / n)
        self.sine = numpy.sin(self.w0)
        self.cosine = numpy.cos(self.w0)
        self.coef = 2.0 * self.cosine


def filter(samples, length, target):

    '''w0 is the target frequnecy of filter in radians'''
    constant = constants()
    constant.compute(target, length)

    '''Compute each sample'''
    first = 0
    second = 0
    third = 0
    for sample in samples:
        first = constant.coef * second - third + sample
        third = second
        second = first

    print(constant.k)
    print(constant.coef)

    '''compute optimized magnitude'''
    mag = numpy.power(second,2) + numpy.power(third,2) - second * third * constant.coef
    magsqrt = numpy.sqrt(mag)
    print(mag)
    print(magsqrt)

'''
160 samples per bit
300 bits
37.5 bytes

length is equal to N in the article ? I think
returns two things? freqs and results

'''
