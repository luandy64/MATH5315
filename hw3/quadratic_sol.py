#!/usr/bin/env python3
"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob3.py for Homework 3
- This script is my implementation of a root finder using interpolating
polynomials to do the work. A choice of using the Newton form of interpolating
was made because it is easier to recompute the values of the coefficients
rather than constantly rebuild polynomials of degree 0 up to n. Helper
functions have been written to improve source code readability.
"""

# Imports
import numpy as np
from math import *

##############################################################################
#                            Function Definitions                            #
##############################################################################

def quadratic_sol(Ffun, x, maxit, Srtol, Satol, Rrtol, Ratol, output):
    """
    Usage: x, its = quadratic_sol( Inputs )
    Inputs:
            Ffun    Nonlinear function name/handle
            x       Initial guess at solution
            maxit   max allowed number of iterations
            Srtol   relative solution tolerance
            Satol   absolute solution tolerance
            Rrtol   relative residual tolerance
            Ratol   absolute residual tolerance
            output  Boolean to output iteration history
    Outputs:
            x       Approximate solution
            its     Number of iterations used
    """

    # Check input arguments, reset values as needed
    if (int(maxit) < 1):
        print("quadratic_sol: maxit = %i < 1. Resetting to 100\n"
              % (int(maxit)))
        maxit = 100
    if (Srtol < 1e-15):
        print("quadratic_sol: Srtol = %g < %g. Resetting to %g\n"
              % (Srtol, 1e-15, 1e-15))
        Srtol = 1e-10
    if (Satol < 0):
        print("quadratic_sol: Satol = %g < 0. Resetting to %g\n"
              % (Satol, 1e-15))
        Satol = 1e-5
    if (Rrtol < 1e-15):
        print("quadratic_sol: Rrtol = %g < %g. Resetting to %g\n"
              % (Rrtol, 1e-15, 1e-15))
        Rrtol = 1e-10
    if (Ratol < 0):
        print("quadratic_sol: Ratol = %g < 0. Resetting to %g\n"
              % (Ratol, 1e-15))
        Ratol = 1e-5

    # Initialize variables
    x0 = x
    f0norm = np.linalg.norm(Ffun(x0))

    # Set up the two other initial guesses
    if (x0 == 0):
        x1 = x + 1e-2
        x2 = x - 1e-2
    else:
        x1 = x*(1 + 1e-2)
        x2 = x*(1 - 1e-2)

    for it in range(1, maxit):
        # Call utility functions to build a quadratic interpolating function
        # clist will be [a, b, c] for ax^2 + bx + c
        clist = newtoncoeff(Ffun, x0, x1, x2)
        # Using a,b,c plug those into the quadratic question and return a root 
        root = quad_equation(clist, x0)

        # Compute norms for convergence checking
        hnorm = np.linalg.norm(root - x0)
        fnorm = np.linalg.norm(Ffun(root))
        xnorm = np.linalg.norm(root)

        # Shift guesses
        x2 = x1
        x1 = x0
        x0 = root

        # Check if convergence history is wanted
        if (output):
            print("   iter %3i, \t||h|| = %g, \thtol = %g,"
                  % (it, hnorm, Satol+Srtol*xnorm), end='')
            print(" \t||f|| = %g, \tftol = %g\n"
                  % (fnorm, Ratol+Rrtol*f0norm), end='')

        # Check for convergence
        if ((hnorm < Satol + Srtol*xnorm) or (fnorm < Ratol + Rrtol*f0norm)):
            break

    return  [x0, it]
def quad_equation(clist, x0):
    """
    Usage: root = quad_equation(clist, x0)
    Inputs:
            clist   A list of coefficients in the order a,b,c for
                      ax^2 + bx + c
            x0      The most recent iterate
    Outputs:
            root    Solution to the quadratic
    """

    if (len(clist) != 3):
        print("quad_equation: Improper Number of Arguments")
        exit()

    # Check if real roots can be found
    if ((pow(clist[1],2) - 4*clist[0]*clist[2]) >= 0):
        # Compute two root using the standard quadratic formula
        posRoot = (-(clist[1]) + sqrt(pow(clist[1],2) 
                   - 4*clist[0]*clist[2])) / (2*clist[0])
        negRoot = (-(clist[1]) - sqrt(pow(clist[1],2) 
                   - 4*clist[0]*clist[2])) / (2*clist[0])

        # Find the root closest to x0
        if (abs(posRoot - x0) < abs(negRoot - x0)):
            root = posRoot
        else:
            root = negRoot

        return root
    else:
        print("quadratic_sol: Imaginary Roots. Exiting")
        exit()

def newtoncoeff(Ffun, x0, x1, x2):
    """
    Usage: clist = newtoncoeff(Ffun, x0, x1, x2)
    Inputs:
            Ffun    Function handle
            x0      A point to interpolate
            x1      A point to interpolate
            x2      A point to interpolate
    Outputs:
            clist   A list of the coefficients that describe the interpolating
                      polynomial
    """
    # calculate divided differences
    c0 = Ffun(x0)
    c1 =  (Ffun(x1) - Ffun(x0)) / (x1 - x0)
    c2 = (Ffun(x2) - c0 - c1*(x2 - x0)) / ((x2 - x0) *(x2 - x1))
    
    # Compute coefficients a, b, c
    a = c2
    b = c1 - c2*x1 - c2*x0
    c = c0 - c1*x0 + c2*x0*x1

    return [a, b, c]
