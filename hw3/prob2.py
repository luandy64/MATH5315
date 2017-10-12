#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob2.py for Homework 3
- This script contains a test of three numerical methods to how they compare
"""

# Imports
from steffensen import *
from newton import *
from quadratic_sol import *
import math
import time

###############################################################################
#                             Function definitions                            #
###############################################################################
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
    print("  Quadratic:")

    # Start computation time
    tstart = time.time()
    x3, its3 = quadratic_sol(f, num, maxit, Srtol, Satol, Rrtol, Ratol, output)
    # Stop time
    ttot = time.time() - tstart

    # Record solution
    print("   final solution = ", x3, ", residual = ", np.abs(f(x3)),
          ", time = ", ttot, ", its = ", its3)
    #--------------------------------------------------------------------------
"""
2
  (a)
    Based on the output history, this method works just about the same as
    Newton's. It out performed Steffensen's method in one test. The one
    difference I saw in Newton's v. Quadratic was in the number of iterations
    it took: Quadratic seemed to take plus or minus 1 iteration compared to 
    Newton's. This could have been just a counting issue in my code.

  (b)
    Just from writing this method, I could think of two reasons why this method
    is not more widely used. First, creating the interpolating polynomials is
    risky; in that, you have to be careful of complex roots that would stop the
    method in its tracks. Second,I bet the Quadratic method does not extend to
    higher dimensions, so why write 2 pieces of code to do 2 jobs, when 1 piece
    of code can do 2 jobs.
"""
