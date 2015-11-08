'''
approximate-pi-montecarlo.py

Approximate pi using a single processor with the Monte-Carlo method

Paul Soper

October 26, 2015
'''

import numpy as np
from numpy import linalg as LA
import sys
import math

n = int(sys.argv[1])

inside = 0

for i in range(0,n):
    xy = np.random.rand(1,2)
    if LA.norm(xy) < 1:
        inside = inside + 1

p = 4.0 * float(inside)/float(n)

error = abs(p - math.pi)

print "Estimate = ", p, "Error = ", error

    
