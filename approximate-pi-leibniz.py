'''
approximate-pi-leibniz.py

Approximate pi using a single processor with the Leibniz formula,
using the bigfloat package

Paul Soper

October 26, 2015
'''

import sys
import math
from bigfloat import *

n = int(sys.argv[1])

with precision(100):
    divisor = BigFloat(1)
    p = BigFloat(0)

    for i in range(0,n/2):
        p = add(p, div(1.0, divisor))
        divisor = add(divisor, 2)
        p = sub(p, div(1.0, divisor))
        divisor = add(divisor, 2)

        if (n % 2) == 1:
            p = add(p, div(1.0, divisor))

    p = mul(p, 4.0)

    error = abs(sub(p, const_pi()))

print "Estimate = ", p
print
print "Error = ", error


                
    

    
