'''
approximate-pi-chudnovsky.py

Approximate pi using a single processor with the Chudnovsky method,
using the bigfloat package

Paul Soper

November 4, 2015
'''

import sys
import math
from bigfloat import *
from scipy.special import factorial

n = int(sys.argv[1])

with precision(200):
    p = BigFloat(0)
    overpi = BigFloat(0)
    
    for k in range(0,n):
        m = (-1)**k
        n1 = factorial(6*k, True)
        n2 = 13591409 + 545140134*k
        d1 = factorial(3*k,True)
        d2 = (factorial(k))**3
        d3 = pow(640320,(3*k+1.5))
        numerator = mul(m,mul(n1,n2))
        denominator = mul(d1,mul(d2,d3))
        term = div(numerator,denominator)
        overpi = add(overpi,term)

    overpi = mul(overpi,12)
    p = div(1,overpi)

    error = abs(sub(p, const_pi()))

print "Estimate = ", p
print
print "Error = ", error


                
    

    
