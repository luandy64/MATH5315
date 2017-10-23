#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

cubic_spline.py for Homework 4
- This file defines two functions:
  (1) cubic_spline_coefficients to calculate the cubic spline coefficients
  (2) cubic_spline_evaluate to evaluate a cubic spline
"""

# Imports
import numpy as np
from scipy import linalg

#################################################################################
#                             Function Definitions                              #
#################################################################################
def cubic_spline_coefficients(t, y, alpha, beta):
    """
    Usage: z = cubic_spline_coefficients(t, y, alpha, beta)
    
    This function solves for and returns the coefficients of the cubic spline 
    that interpolates the points (t,y) and satisfies the boundary conditions
    S''(t0) = alpha and S'(tn) = beta.
    
    Inputs:    t        A vector of knots
               y        A vector of the y values at the knots
               alpha    A boundary condition: S''(t0) = alpha
               beta     A boundary condition: S'(tn) = beta
    Output:    z        A vector of the coefficients of the cubic spline 
                          interpolant
    """
    # Get the size of vector t
    n = len(t)
    
    # Create a zero matrix of size NxN
    tridiag = np.zeros(n)
    
    # Create a zero vector of size N
    z = np.zeros(n)
    
    # Create a zero vector of size N
    v = np.zeros(n)
    
    # Fill the values of the tridiagonal matrix
    
    # Fill entry [0,0]
    tridiag[0,0] = 1.0
    
    # Fill entries [i,j] where i,j = 1,...,n-1 
    for i in range(1,n):
        # Compute value for h_i-1
        hleft = t[i] - t[i-1]
        
        # Compute value for h_i
        hright = t[i+1] - t[i]
        
        # Fill the entry to the left of the diagonal 
        tridiag[i, (i-1)] = hleft
        
        # Fill the entry on the diagonal
        tridiag[i,i] = 2*(hleft - hright)
        
        # Fill the entry to the right of the diagonal
        tridiag[i, (i+1)] = hright
    
    # Calculate h(n-1) to use in the last row of tridiag
    hleft = t[n-1] - t[n]
    
    # Fill entry [n-1,n-2]
    tridiag[(n-1),(n-2)] = hleft
    
    # Fill entry [n-1,n-1]
    tridiag[(n-1),(n-1)] = 2* hleft
    
    # Fill values of vector v
    
    # Fill v[0]
    v[0] = alpha
    
    # Fill v[i] where i = 1, n-1
    for i in range(1,n):
        # Compute value for h_i-1
        hleft = t[i] - t[i-1]
        
        # Compute value for h_i
        hright = t[i+1] - t[i]
        
        # Compute value for v_i
        v[i] = (6/hright)*(y[(i+1)]-y[i]) - (6/hleft)*(y[i]-y[(i-1)])
        
    # Fill v[n]
    v[n] = 6 * beta - 6*(y[n] - y[n-1]) / hleft
    
    
    
def cubic_spline_evaluate(t, y, z, x):
    """
    Usage: s = cubic spline_evaluate(t, y, z, x)
    
    This function evaluates S(x), the cubic spline interpolant.
    
    Inputs:    t        A vector of knots
               y        A vector of the y values at the knots
               z        A vector of the coefficients of the cubic spline 
                          interpolant
               x        The value to evaluate the interpolant at
    Output:    s        The value of the interpolant at x
    """