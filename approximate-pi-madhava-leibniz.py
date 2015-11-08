'''
approximate-pi-madhava-leibniz.py

Approximate pi using a single processor with the Madhava-Leibniz method,
using the bigfloat package

Paul Soper

November 4, 2015
'''

import sys
import math
from bigfloat import *

n = int(sys.argv[1])

with precision(100):
    p = BigFloat(0)

    for k in range(0,n):
        term = pow(div(-1,3),k)
        term = div(term,add(mul(2,k),1))
        p = add(p,term)

    p = mul(p, sqrt(12))

    error = abs(sub(p, const_pi()))

print "Estimate = ", p
print
print "Error = ", error


                
    

    
