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