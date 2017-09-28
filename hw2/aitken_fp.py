#!/usr/bin/en python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

aitken_fp.py for Homework 2
- This script was written to implement an Aitken Extrapolation
"""

# Imports
import numpy as np

#################################################################################
#                              Function Declaration                             #
#################################################################################
def aitken_fp(Gfun, x, maxit, rtol, atol, output):
    """
    Usage: x, its = aitken_fp(Gfun, x, maxit, rtol, atol, output)

    This function uses a given function Gfun to perform a fixed point iteration
    x_k+1 = g(x_k) using the Aitken Extrapolation.The iteration stops when the 
    following condition is met:

           ||x_k+1 - x_k|| < atol + rtol*||x_k||

    Inputs:   Gfun     Fixed Point Iteration function name/handle
              x        initial guess at solution
              maxit    maximum number of iterations allowed
              rtol     relative tolerance
              atol     absolute tolerance
              output   boolean to output iteration history/plot
    Outputs:  xnew     approximation
              its      number of iterations needed
    """
    
    # Checking Inputs
    if (int(maxit) < 1):
        print("aitken_fp: maxit = %i < 1. Resetting to 100\n" % (int(maxit)))
        maxit = 100
    if (rtol < 1e-15):
        print("aitken_fp: rtol = %g < %g. Resetting to %g\n"
              % (rtol, 1e-15, 1e-10))
        rtol = 1e-10
    if (atol < 0):
        print("aitken_fp: atol = %g < 0. Resetting to %g\n"% (atol, 1e-15))
        atol = 1e-5
        
    # Initialize variables
    xold = x    # x_k
    xnew = x    # x_k+1
    
    # Perform the iteration
    for i in range(1, maxit):
        # Computing the extrapolating points
        y = Gfun(xnew)
        z = Gfun(y)
        
        # Save x_k+1 as x_k
        xold = xnew
        
        # Update x_k+1
        xnew = (z*xold - y*y) / (xold - 2*y + z)
        
        # Compute norms
        ltnorm = np.linalg.norm(xnew - xold)
        rtnorm = np.linalg.norm(xold)
        
        # Check if convergence history is wanted
        if (output):
            print("   iter %3i, \t||xnew - xold|| = %g," % (i,ltnorm), end='')
            print("\tatol + rtol||xold|| = %g\n" % (atol + rtol*(rtnorm)), end='')
        # Checking exit condition
        if (ltnorm < atol + rtol*rtnorm):
            break
    
    return [xnew, i]
        