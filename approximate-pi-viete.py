'''
approximate-pi-viete.py

Approximate pi using a single processor with the Viete's formula
and the BigFloat package

Paul Soper

October 26, 2015
'''

import sys
import math
from bigfloat import *

n = int(sys.argv[1])

with precision(1000):
    a = [sqrt(2.0)]

    for i in range(1,n):
        a.append(sqrt(add(a[i-1], 2.0)))

        q = map(lambda x:div(x,2.0), a)
        r = reduce(lambda x,y:mul(x, y), q)
        p = div(2.0, r)

    error = abs(p - const_pi())

print
print "Estimate = ", p
print
print "Error = ", error

    
