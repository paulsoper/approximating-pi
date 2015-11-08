'''
approximate-pi-ramanujan.py

Approximate pi using a single processor with the Ramanujan method,
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
        n1 = factorial(4*k, True)
        n2 = 1103 + 26390*k
        d1 = factorial(k,True)**4
        d2 = 396**(4*k)
        term = div(mul(n1,n2),mul(d1,d2))
        overpi = add(overpi,term)

    m1 = div(mul(2,sqrt(2)),9801)
    overpi = mul(overpi,m1)
    p = div(1,overpi)

    error = abs(sub(p, const_pi()))

print "Estimate = ", p
print
print "Error = ", error


                
    

    
