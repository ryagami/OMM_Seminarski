import cmath
import numpy as np
from math import sqrt
from mpmath import ellipk, re
import matplotlib.pyplot as plt


def period(k, j, alpha):
    el_int = re(ellipk(complex(0, alpha ** 2 * j / (2 * k + alpha ** 2 * j))))
    p = 4 * sqrt(2) * el_int / sqrt(2 * k + alpha ** 2 * j)
    return p


def period_array(k, j, t_range, step):
    alpha = np.arange(0, t_range, step)

    n = alpha.size

    p = np.zeros(n)

    for i in range(n):
        p[i] = period(k, j, alpha[i])

    return {
        'alpha': alpha,
        'period': p
    }
