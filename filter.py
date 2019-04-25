import numpy

RATE = 48000

'''Implementation is of optimized version from
   https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm
'''

class constants:
    '''class to hold data on  norm and coefficients'''
    coef = 0
    cosine = 0
    sine = 0
    k = 0
    w0 = 0
    def compute(self, freq, n):
        k = ((n * freq)/ RATE)
        w0 = ((2*numpy.pi*k) / n)
        sine = numpy.sin(w0)
        cosine = numpy.cos(w0)
        coef = 2.0 * cosine


def filter(samples, length, target):

    '''w0 is the target frequnecy of filter in radians'''
    constant = constants()
    x = constant.compute(target, length)

    '''Compute each sample'''
    first = 0
    second = 0
    third = 0
    for sample in samples:
        first = constant.coef * second - third + sample
        third = second
        second = first

    '''compute optimized magnitude'''
    mag = nupmy.power(second,2) + numpy.power(third,2) - second * third * constant.coef

'''
160 samples per bit
300 bits
37.5 bytes

length is equal to N in the article ? I think
returns two things? freqs and results

'''

print(numpy.power(5,2))
print(5*5)
