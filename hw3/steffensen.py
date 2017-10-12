#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

steffensen.py for Homework 2
- This script contains a function steffensen() to carry out Steffensen's method
"""
# Imports
import numpy as np
import math

################################################################################
#                             Function Definition(s)                           #
################################################################################
def g(x, f):
    """
    Usage: gx = g(x, Ffun)
    
    This function computes a first order forward finite difference of Ffun at
    x. 
    
    Inputs:     x       x value we want to evaluate
                Ffun    Function name/handle
    Outputs:    gx      approximation
    """
    g =   ( f(f(x) + x) - f(x) ) / (f(x)) 
    return g

def steffensen(Ffun, x, maxit, Srtol, Satol, Rrtol, Ratol, output):
    """
    Usage: x, its = steffensen(Ffun, x, maxit, 
                               Srtol, Satol, Rrtol, Ratol, output)

    This function uses Steffensen's method to find the root of a nonlinear 
    system of equations F(x)=0. The iteration stops when the following 
    condition is met:

           ||x_k+1 - x_k|| < atol + rtol*||x_k||

    Inputs:   Ffun     nonlinear function name/handle
              x        initial guess at solution
              maxit    maximum number of iterations allowed
              Srtol    solution relative tolerance
              Satol    solution absolute tolerance
              Rrtol    residual relative tolerance
              Ratol    residual absolute tolerance
              output   boolean to output iteration history/plot
    Outputs:  x        approximation
              its      number of iterations needed
    """
    # check input arguments
    if (int(maxit) < 1):
        print("Steffensen: maxit = %i < 1. Resetting to 10\n" 
              % (int(maxit)))
        maxit = 10
    if (Srtol < 1e-15):
        print("Steffensen: Srtol = %g < %g. Resetting to %g\n" 
              % (Srtol, 1e-15, 1e-15))
        Srtol = 1e-15
    if (Satol < 0):
        print("Steffensen: Satol = %g < 0. Resetting to %g\n" 
              % (Satol, 1e-15))
        Satol = 1e-15
    if (Rrtol < 1e-15):
        print("Steffensen: Rrtol = %g < %g. Resetting to %g\n" 
              % (Rrtol, 1e-15, 1e-15))
        Rrtol = 1e-15
    if (Ratol < 0):
        print("Steffensen: Ratol = %g < 0. Resetting to %g\n" 
              % (Ratol, 1e-15))
        Ratol = 1e-15
    
    # Comopute f(x)
    F = Ffun(x)
    
    # Compute the finite difference g~(x)
    gtilde = g(x, Ffun)
    
    # Divide f(x) by g~(x)
    h = F / gtilde
    
    # Initialize variables
    xold = x                # x_k
    xnew = x - h            # x_k+1
    
    # Compute the norm of the first iteration
    f0norm = np.linalg.norm(xnew)
    
    # Run the iteration
    for its in range(2, maxit+1):
    
        # Compute the finite difference g~(x)
        gtilde = g(xnew, Ffun)
        
        # Compute the x update
        h = F / gtilde
        
        # Store x_k+1 as x_k
        xold = xnew
        
        # Update x_k+1
        xnew = xold - h

        F = Ffun(xnew)
        
        # Check for convergence
        hnorm = np.linalg.norm(h)
        xnorm = np.linalg.norm(xnew)
        fnorm = np.linalg.norm(F)
        
        # Check if convergence history is wanted
        if (output):
            print("   iter %3i, \t||h|| = %g, \thtol = %g," 
                  % (its, hnorm, Satol+Srtol*xnorm), end='')
            print(" \t||f|| = %g, \tftol = %g\n" 
                  % (fnorm, Ratol+Rrtol*f0norm), end='')
        
        # Check for exit condition
        if ( (hnorm < Satol + Srtol*xnorm) or (fnorm < Ratol + Rrtol*f0norm)):
            break
        
    return [xnew, its]
    
    
    