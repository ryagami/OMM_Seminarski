import cmath
import numpy as np
from math import sqrt
from mpmath import ellipk, re
import matplotlib.pyplot as plt 

def period(k, j, t_range, step): 
    alfa = np.arange(0, t_range, step)

    n = alfa.size

    period = np.zeros(n)

    for i in range(n):
        el_int = re(ellipk(complex( 0, alfa[i]**2 * j / (2 * k + alfa[i]**2 * j))))
        period[i] =  4 * sqrt(2) * el_int / sqrt(2 * k + alfa[i]**2 + j)

    return {
        'alfa': alfa,
        'period': period
    }


    