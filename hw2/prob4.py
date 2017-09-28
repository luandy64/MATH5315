#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob4.py for Homework 2
- This script was written by Daniel R. Reynolds, but modified by Andy Lu to
  make Ffun() only need one parameter.
"""

# Imports
import numpy as np
import math
from aitken_fp import *
from fixed_point import *
import time

#################################################################################
#                              Function definitions                             #
#################################################################################
def ga(x):
    """
    Usage: gx = g(x)
    
    This function computes f(x) = (1/4)x^2 - (1/2)x - 1
    
    Inputs:     x       x value we want to evaluate
    Outputs:    gx      approximation
    """
    g = (0.25)*x*x - (0.5)*x - 1
    return g
    
def gb(x):
    """
    Usage: gx = g(x)
    
    This function computes f(x) = cos(x)
    
    Inputs:     x       x value we want to evaluate
    Outputs:    gx      approximation
    """
    g = math.cos(x)
    return g
    
def gc(x):
    """
    Usage: gx = g(x)
    
    This function computes f(x) = (1/2)[(3/x) - x]
    
    Inputs:     x       x value we want to evaluate
    Outputs:    gx      approximation
    """
    g = (0.5)*(3/x + x)
    return g
    
def gd(x):
    """
    Usage: gx = g(x)
    
    This function computes f(x) = (1/4)x^2 - (1/2)x - 1
    
    Inputs:     x       x value we want to evaluate
    Outputs:    gx      approximation
    """
    g = math.cosh(x) / x - math.atan(x)
    return g

def divider():
    """
    Usage: divider()
    
    This function prints 80 dashes to separate output throughout this program
    
    Inputs:     N/A
    Outputs:    (to screen) 80 '-'
    """
    print("----------------------------------------"+
          "----------------------------------------")
    
#################################################################################
#                                  Main Driver                                  #
#################################################################################

# Initialize variables to run tests
index = ['A', 'B', 'C', 'D']
gfunc = [ga, gb, gc, gd]
x0 = 2
maxit = 100
rtol = 1e-10
atol = 1e-5
output = True

for i in range(4):
    #--------------------------------------------------------------------------
    # Print divider for readability
    divider()
    
    # State Subproblem letter
    print("Problem {}:".format(index[i]))
    
    print("fixed_point()")
    
    # Start time
    tstart = time.time()
    x1, its1 = fixed_point(gfunc[i], x0, maxit, rtol, atol, output)
    
    # Stop time
    ttot = time.time() - tstart
    
    # Record solution
    print("   final solution = ", x1, ", residual = ", np.abs(gfunc[i](x1)), 
          ", time = ", ttot, ", its = ", its1)
    #--------------------------------------------------------------------------
    print("aitken_fp()")
    
    # Start time
    tstart = time.time()
    x2, its2 = aitken_fp(gfunc[i], x0, maxit, rtol, atol, output)
    
    # Stop time
    ttot = time.time() - tstart
    
    # Record solution
    print("   final solution = ", x2, ", residual = ", np.abs(gfunc[i](x2)), 
          ", time = ", ttot, ", its = ", its2)
    #--------------------------------------------------------------------------

# Print divider for readability
divider()
print("The standard fixed point for the last problem didn't converge to the" +
" root and instead converged to 0.58. Since the output history shows the same" +
" value over and over, I think a point where 1/2 cosh(x) = 0 or arctan(x) = 0" +
". Thus whatever was the value is at the nonzero portion is the number we" +
" converge to.")