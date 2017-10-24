#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

Runge_spline_test.py for Homework 4
- This file creates the cubic spline interpolant of the Runge function, 
  f(x) = 1/(1+x^2), using equally spaced knots between [-3,3].
"""

# Imports
import numpy as np
from cubic_spline import *
import matplotlib.pyplot as plt
################################################################################
#                              Function Definition                             #
################################################################################

def f(x):
    return 1./(1+(x*x))

################################################################################
#                                 Main Driver                                  #
################################################################################

# Initialize variables
n = [4, 16, 64]
alpha = 0.052
beta = -0.06

# Create vectors of knots, adding one accounts for 0
t4 = np.zeros(n[0]+1)
t16 = np.zeros(n[1]+1)
t64 = np.zeros(n[2]+1)

# Fill in knot values
for i in range(n[2]+1):
    if i < n[0]+1:
        t4[i] = (-3) + i*(6/n[0])
    if i < n[1]+1:
        t16[i] = (-3) + i*(6/n[1])
    if i < n[2]+1:
        t64[i] = (-3) + i*(6/n[2]) 

# Create vectors to store function values at knots
y4 = np.zeros(n[0]+1)
y16 = np.zeros(n[1]+1)
y64 = np.zeros(n[2]+1)

for i in range(n[2]+1):
    if i < n[0]+1:
        y4[i] = f(t4[i])
    if i < n[1]+1:
        y16[i] = f(t16[i])
    if i < n[2]+1:
        y64[i] = f(t64[i])

# Create vectors to store spline coefficients
z4 = cubic_spline_coefficients(t4, y4, alpha, beta)
z16 = cubic_spline_coefficients(t16, y16, alpha, beta)
z64 = cubic_spline_coefficients(t64, y64, alpha, beta)

# Evaluate spline functions at 200 points
xval = np.linspace(-3.0, 3.0, num=200)

s4 = np.zeros(200)
s16 = np.zeros(200)
s64 = np.zeros(200)

counter = 0
for x in xval:
    s4[counter] = cubic_spline_evaluate(t4, y4, z4, x)
    s16[counter] = cubic_spline_evaluate(t16, y16, z16, x)
    s64[counter] = cubic_spline_evaluate(t64, y64, z64, x)
    counter = counter + 1

################################################################################
#                                 Plotting S4                                  #
################################################################################
plt.plot(xval,s4,'b', label='S(x)')
plt.plot(xval, f(xval),'r--', label=r"$f(x)=\frac{1}{1+x^2}$")
plt.title('Cubic Spline Interpolant: n=4')
plt.legend()
plt.draw()
plt.figure()
plt.title('Cubic Spline Interpolant Eror: n=4')
plt.semilogy(xval, abs(f(xval) - s4), 'r-')
plt.draw()
plt.figure()

################################################################################
#                                 Plotting S16                                 #
################################################################################
plt.plot(xval,s16,'b', label='S(x)')
plt.plot(xval, f(xval),'r--', label=r"$f(x)=\frac{1}{1+x^2}$")
plt.title('Cubic Spline Interpolant: n=16')
plt.legend()
plt.draw()
plt.figure()
plt.title('Cubic Spline Interpolant Eror: n=16')
plt.semilogy(xval, abs(f(xval) - s16), 'r-')
plt.draw()
plt.figure()    

################################################################################
#                                 Plotting S64                                 #
################################################################################
plt.plot(xval,s64,'b', label='S(x)')
plt.plot(xval, f(xval),'r--', label=r"$f(x)=\frac{1}{1+x^2}$")
plt.title('Cubic Spline Interpolant: n=64')
plt.legend()
plt.draw()
plt.figure()
plt.title('Cubic Spline Interpolant Eror: n=64')
plt.semilogy(xval, abs(f(xval) - s64), 'r-')
plt.show()

################################################################################
#                                   Comments                                   #
################################################################################
# The problem is the Lagrange interpolant uses a high order polynomial to make 
# sure all of the nodes are interpolated. This results in more and more
# oscilation the farther from the orgin you move. Thus the end points at the 
# boundary are oscilating in the Lagrange; on the other hand, the cubic splines 
# are piecewise defined on subintervals. However, they are at most degree 3, 
# which is much less oscilatory than whatever the Lagrange is.

