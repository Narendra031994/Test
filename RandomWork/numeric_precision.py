""" 
truncate - Function removes all the digits after the decimal point.
ceil = largest integer greater than or equal to x
floor - largest integer <= x
round - round off the float.
"""
from fractions import Fraction
import math
rational = Fraction(3,4,_normalize=True)
format(float(rational),'.5f') # this will display 5 digits after the decimal point
real = float(rational)
round(real,1)# This is routing upto 1 degit after the decimal point
# bankers rounding
round(0.25,1)# Number will be rounded to the integer with even LSB 10^(-1) = 0.1
math.trunc(1.0014475556858)
math.ceil(10.9)
math.floor(10.2)



