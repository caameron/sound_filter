import numpy

RATE = 48000

'''https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm'''

class constants:
    '''class to hold data on  norm and coefficients'''
    coef = 0
    cosine = 0
    sine = 0
    def compute(self, freq, n):
        k = ((n * freq)/ RATE)
        w0 = ((2*numpy.pi*k) / n)
        sine = numpy.sin(w0)
        cosine = numpy.cos(w0)
        coef = 2.0 * cosine


def filter(samples, length, target):

    '''w0 is the target frequnecy of filter in radians'''
    c1 = constants()
    x = c1.compute(target, length)

    '''Compute each sample'''


'''
160 samples per bit
300 bits
37.5 bytes

length is equal to N in the article ? I think
returns two things? freqs and results

'''

filter(1, 205, 941)
