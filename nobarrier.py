import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    time.sleep(10)
print ("process " + str(rank) + " is here")