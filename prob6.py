#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob6.py for Homework 1
- This script finds machines numbers
"""
# Imports
import numpy as np
from math import *
import warnings

# To suppress the warning from finding the largest single precision number
warnings.filterwarnings("ignore")

###############################################################################
#                              Single Precision                               #
###############################################################################

# Declarations
one = np.float32(1.0)
two = np.float32(2.0)
epS = np.float32(1.0)
smallS = np.float32(1.0)
largeS = np.float32(1.0)
maxit = 1000000000

# Find machine precision
for i in range(maxit):
    if(one + epS <= one):
        break
    else:
        epS = epS / two

# Find Smallest Positive machine number
for i in range(maxit):
    if (smallS / two == 0.0):
        break
    else:
        smallS = smallS / two

# Find Largest Positive machine number
for i in range(maxit):
    
    if isinf(largeS * two):
        break

    else:
        largeS = largeS * two

###############################################################################
#                              Double Precision                               #
###############################################################################
# Declarations
epD = 1.0
smallD = 1.0
largeD = 1.0

# Find machine precision
for i in range(maxit):
    if(1.0 + epD <= 1.0):
        break
    else:
        epD = epD / 2.0

# Find Smallest Positive machine number
for i in range(maxit):
    if (smallD / 2.0 == 0.0):
        break
    else:
        smallD = smallD / 2.0

# Find Largest Positive machine number
for i in range(maxit):
    if (largeD * 2.0 >= np.inf):
        break
    else:
        largeD = largeD * 2.0
###############################################################################
#                                   Output                                    #
###############################################################################
print("(a)")
print("\tSingle: {}".format(epS))
print("\tDouble: {}".format(epD))

print("(b)")
print("\tSingle: {}".format(largeS))
print("\tDouble: {}".format(largeD))

print("(c)")
print("\tSingle: {}".format(smallS))
print("\tDouble: {}".format(smallD))