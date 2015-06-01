#This code snippet sums all of the self power from 1 to any arbitrary
#number n and returns the sum m

from numpy import *

def powers(n):
    m = 0
    for i in range(1,n):
        m += (i**i)
    return m
