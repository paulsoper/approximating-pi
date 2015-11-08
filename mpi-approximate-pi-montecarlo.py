'''
mpi-approximate-pi-montecarlo.py

Approximate pi using multieple processors and MPI with the Monte-Carlo method

Paul Soper

October 26, 2015
'''

import numpy as np
from numpy import linalg as LA
import sys
import math
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1])

if (rank == 0):
    if (n % size) <> 0:
        print "Error - number of calculations must be a multiple of the number of nodes"
        print "Exiting ..."
        comm.Abort()

local_n = n/size

inside = np.zeros(1)

local_inside = np.zeros(1)

for i in range(0,local_n):
    xy = np.random.rand(1,2)
    if LA.norm(xy) < 1:
        local_inside[0] = local_inside[0] + 1

comm.Reduce(local_inside, inside, op=MPI.SUM)

if (rank == 0):
    p = 4.0 * float(inside[0])/float(n)    
    error = abs(p - math.pi)
    print "Estimate = ", p, "Error = ", error

MPI.Finalize()

