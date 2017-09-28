#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob3.py for Homework 2
- This script contains a test of two numerical methods to see which is more
  efficient
"""

# Imports
from steffensen import *
from newton import *
import math
import time

#################################################################################
#                              Function definitions                             #
#################################################################################
def f(x):
    """
    Usage: fx = f(x)
    
    This function computes f(x) = e^(x/2) - 3x - 2
    
    Inputs:     x       x value we want to evaluate
    Outputs:    fx      approximation
    """
    f = math.exp(x/2) - 3*x - 2 
    return f

def J(x):
    """
    Usage: Jx = J(x)
    
    This function computes f(x) = (1/2)e^(x/2) - 3x - 2
    
    Inputs:     x       x value we want to evaluate
    Outputs:    Jx      approximation
    """
    J = (math.exp(x/2) / 2) - 3
    return J
    
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
# Initializing variables to run tests
output = True
maxit = 50
Satol = 1e-6
Srtol = 1e-6
Ratol = 1e-13
Rrtol = 1e-13
x0 = [-5, 2, 5]

for num in x0:
    divider()
    #--------------------------------------------------------------------------
    print("  Newton:")
    
    # Start computation time
    tstart = time.time()
    x1, its1 = newton(f, J, num, maxit, Srtol, Satol, Rrtol, Ratol, output)
    # Stop time
    ttot = time.time() - tstart
    
    # Record solution
    print("   final solution = ", x1, ", residual = ", np.abs(f(x1)), 
          ", time = ", ttot, ", its = ", its1)
    #--------------------------------------------------------------------------
    print("  Steffensen:")
    
    # Start computation time
    tstart = time.time()
    x2, its2 = steffensen(f, num, maxit, Srtol, Satol, Rrtol, Ratol, output)
    # Stop time
    ttot = time.time() - tstart
    
    # Record solution
    print("   final solution = ", x2, ", residual = ", np.abs(f(x2)), 
          ", time = ", ttot, ", its = ", its2)
    #--------------------------------------------------------------------------

# Print a divider for readability
divider()
# Paragraph explaining results
print("From the output history, it seems like the first iteration"+
" (of the first problem) caused" +
" Steffensen's to shift the guesses far to one side. It's likely that the" +
" graph around that area has a super steep slope, causing the models we" +
" build to find new guesses right next to the pervious guess. So with each" +
" iteration, we are only inching along a section where we are no where near" +
" the roots.")