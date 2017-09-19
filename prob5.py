#!/usr/bin/env python3

"""
Andy Lu
SMU Mathematics
MATH 5315 Fall 2017

prob5.py for Homework 1
- This script demonstrates that some function f(x) converges with order g(x)
"""
# Imports
from math import *


###############################################################################
#                              Class Definition                               #
###############################################################################
class SubProb():
    """
    This class contains 3 attributes to store the results of calculations
        easily and to increase readability of the code
    
    Declaration:
    varname = SubProb(letter, 'O')
      - letter is a single char indicating the subproblem letter
      - 'O' may be 'o'
    
    setF(inputString):
      - inputString is a sting version of the function in the question
    
    setG(inputString):
      - inputString is a sting version of the function in the question
    
    getF():
      - returns the string stored in self.f
    
    getG():
      - returns the string stored in self.g
    
    summerize():
      - Calling this function will neatly print the attributes of this class
        into 3 columns (with no column heading)
        {f}      {g}    {c}
      - f is the string representing the function f(x)
      - g is the function representing O(g(x))
      - c is either a number f(x)/g(x) converges to or it is zero
    """
    
    def __init__(self, letter, bigO = 'O'):
        # probLetter denotes which subproblem this is
        self.probLetter = letter
        
        # f(x) = O(g(x))
        # f represents the left equation
        # g represents the right equation
        self.f = ''
        self.g = ''
        
        # c represents the constant that is converged to
        self.c = -1
        
        # type is a string representing O or o
        self.type = bigO
        
    # Function 'setF()' sets f equal to the input string
    def setF(self, inputString):
        self.f = inputString
        
    # Function 'setG()' sets g equal to the input string
    def setG(self, inputString):
        self.g = self.type + "(" + inputString + ")"
        
    # Function 'getF()' prints the string f
    def getF(self):
        if(self.f == ''):
            print("getF Error: No function set for f")
        else:
            return self.f
        
    # Function 'getG()' prints the string g 
    def getG(self):
        if(self.g == ''):
            print("getG Error: No function set for g")
        else:
            return self.g
    
    def setC(self, num):
        self.c = num
            
    def summerize(self):
        print("(" + self.probLetter + ")")
        #print("{0:>}    {1:>}    {2:>}".format(self.f, self.g, self.c))
        print(self.f.rjust(15) + self.g.rjust(15) + str(self.c).rjust(30))
        
###############################################################################
#                              Begin Main Script                              #
###############################################################################
# A dividerLine to improve output readability
dividerLine = '----------------------------------------'

# Setting up data structures
a = SubProb('a', 'O')
b = SubProb('b', 'o')
c = SubProb('c', 'o')
d = SubProb('d', 'O')
e = SubProb('e', 'o')
numer = 0
denom = 0
ans = 0

# Initialize problems
a.setF('(n+1) / n^2')
a.setG('1/n')
b.setF('1/(n ln n)')
b.setG('1/n')
c.setF('1/n')
c.setG('1/(ln n)')
d.setF('5/n + e^(-n)')
d.setG('1/n')
e.setF('e^-n')
e.setG('1/(n^2)')

# Run Tests
print(dividerLine) ############################################################
print("(a): " + a.getF() + " = " + a.getG())
for i in range(1, 100000, 10000):
    numer = (i+1) / i**2
    denom = 1/i
    ans = numer/denom
    
    a.setC(ans)
    
    print("c = " + str(ans))
print(dividerLine) ############################################################
print("(b): " + b.getF() + " = " + b.getG())
vals = [int(pow(2,100)),int(pow(2,200)),int(pow(2,300)),int(pow(2,400)),
        int(pow(2,500)),int(pow(2,600)),int(pow(2,700)),int(pow(2,900)),
        int(pow(2,1014)),int(pow(2,1016))]
for i in vals:
    numer = 1/(i * log(i))
    denom = 1/i
    ans = numer/denom
    
    b.setC(ans)
    
    print("c = " + str(ans))
print(dividerLine) ############################################################
print("(c): " + c.getF() + " = " + c.getG())
#for i in range(int(pow(10,304)), int(pow(2,1016)), int(pow(10,304))):
for i in vals:
    numer = 1/i
    denom = 1/ (log(i))
    ans = numer/denom
    
    c.setC(ans)
    
    print("c = " + str(ans))
print(dividerLine) ############################################################
print("(d): " + d.getF() + " = " + d.getG())
for i in range(1, 40, 4):
    numer = (5/i) + exp(-i)
    denom = 1/i
    ans = numer/denom
    
    d.setC(ans)
    
    print("c = " + str(ans))
print(dividerLine) ############################################################
print("(e): " + e.getF() + " = " + e.getG())
for i in range(1, 900, 90):
    numer = exp(-i)
    denom = 1/(i*i)
    ans = numer/denom
    
    e.setC(ans)
    
    print("c = " + str(ans))
print(dividerLine) ############################################################
print("Summary")
print("")
print("f(x)".center(20) + "O/o(g(x))".center(15) + "c".center(34))
a.summerize()
#print("")
b.summerize()
#print("")
c.summerize()
#print("")
d.summerize()
#print("")
e.summerize()




