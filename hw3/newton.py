#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

newton.py for Homework 2
- This script was written by Daniel R. Reynolds, but modified by Andy Lu to
  make Ffun() only need one parameter.
"""

def newton(Ffun, Jfun, x, maxit, Srtol, Satol, Rrtol, Ratol, output):

    # imports
    import numpy as np
    import math
    import sys

    # check input arguments
    if (int(maxit) < 1):
        sys.stdout.write("newton: maxit = %i < 1. Resetting to 10\n" % (int(maxit)))
        maxit = 10
    if (Srtol < 1e-15):
        sys.stdout.write("newton: Srtol = %g < %g. Resetting to %g\n" % (Srtol, 1e-15, 1e-15))
        Srtol = 1e-15
    if (Satol < 0):
        sys.stdout.write("newton: Satol = %g < 0. Resetting to %g\n" % (Satol, 1e-15))
        Satol = 1e-15
    if (Rrtol < 1e-15):
        sys.stdout.write("newton: Rrtol = %g < %g. Resetting to %g\n" % (Rrtol, 1e-15, 1e-15))
        Rrtol = 1e-15
    if (Ratol < 0):
        sys.stdout.write("newton: Ratol = %g < 0. Resetting to %g\n" % (Ratol, 1e-15))
        Ratol = 1e-15

    # evaluate function for x0
    F = Ffun(x)
    f0norm = np.linalg.norm(F)
        
    # perform iteration
    for its in range(1,maxit+1):

        # evaluate derivative
        J = Jfun(x)

        # compute Newton update, new guess at solution, new residual
        h = F/J
        
        x = x - h
        F = Ffun(x)

        # check for convergence and output diagnostics
        hnorm = np.linalg.norm(h)
        xnorm = np.linalg.norm(x)
        fnorm = np.linalg.norm(F)
        if (output):
            sys.stdout.write("   iter %3i, \t||h|| = %g, \thtol = %g, \t||f|| = %g, \tftol = %g\n" % 
                             (its, hnorm, Satol+Srtol*xnorm, fnorm, Ratol+Rrtol*f0norm))

        if ( (hnorm < Satol + Srtol*xnorm) or (fnorm < Ratol + Rrtol*f0norm)):
            break

    return [x, its]
