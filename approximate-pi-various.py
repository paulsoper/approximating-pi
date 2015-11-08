'''
approximate-pi-various.py

Approximate pi using various simple methods
and the BigFloat package

Paul Soper

November 4, 2015
'''

import sys
import math
from bigfloat import *

with precision(100):
    p = BigFloat(3)
    error = abs(sub(p, const_pi()))
    print "Babylonian - pi ~ 3"
    print "Estimate = ", p
    print "Error = ", error
    print
    
    p = div(22,7)
    error = abs(sub(p, const_pi()))
    print "from Egypt? - pi ~ 22/7"
    print "Estimate = ", p
    print "Error = ", error
    print

    p = div(25,8)
    error = abs(sub(p, const_pi()))
    print "Babylonian Susa - pi ~ 25/8"
    print "Estimate = ", p
    print "Error = ", error
    print
    
    p = div(256,81)
    error = abs(sub(p, const_pi()))
    print "Rhind Papyrus - pi ~ 256/81"
    print "Estimate = ", p
    print "Error = ", error
    print
    
    p = div(339,108)
    error = abs(sub(p, const_pi()))
    print "Shatapatha Brahmana - pi ~ 339/108"
    print "Estimate = ", p
    print "Error = ", error
    print
    
    p = div(223,71)
    error1 = abs(sub(p, const_pi()))
    error2 = abs(sub(div(22,7), const_pi()))
    print "Archimedes - 223/71 < pi < 22/7"
    print "Estimate: pi > ", div(223,71)
    print "Estimate: pi < ", div(22,7)
    print "Lower difference: ", error1
    print "Upper difference: ", error2
    print
    
    p = div(377,120)
    error = abs(sub(p, const_pi()))
    print "Ptolemy - pi ~ 377/120"
    print "Estimate = ", p
    print "Error = ", error
    print

    p = div(3927,1250)
    error = abs(sub(p, const_pi()))
    print "Liu Hui or Zhu Chongzhi - pi ~ 3927/1250"
    print "Estimate = ", p
    print "Error = ", error
    print
    
    p = div(355,113)
    error = abs(sub(p, const_pi()))
    print "Zhu Chongzi - pi ~ 355/113"
    print "Estimate = ", p
    print "Error = ", error
    print

    p = div(62832,20000)
    error = abs(sub(p, const_pi()))
    print "Aryabhata - pi ~ 62832/20000"
    print "Estimate = ", p
    print "Error = ", error
    print
