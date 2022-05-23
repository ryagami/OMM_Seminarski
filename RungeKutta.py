import sys
from numpy import *

def rk(userfun, t_range, u0, step, order=4):

    t = arange(0, t_range + step, step)
    n = len(t)
    m = len(u0)

    u = zeros((m, n))
    u[:, 0] = u0

    beta = zeros((int(order), int(order)))

    # Izbor reda Runge-Kutta metode
    # Podrazumevani red metode je 4
    if order == 1:
        alpha = 0
        beta = 1
        p = 1
    elif order == 2:
        alpha = array([0, 1])
        beta[0, 0] = 1
        beta[1, 0] = 1
        p = array([1 / 2, 1 / 2])
    elif order == 2.1:
        alpha = array([0, 1 / 2])
        beta[0, 0] = 1
        beta[1, 0] = 1 / 2
        p = array([0, 1])
    elif order == 3:
        alpha = array([0, 1 / 2, 1])
        beta[0, 0] = 1
        beta[1, 0] = 1 / 2
        beta[2, 0] = -1
        beta[2, 1] = 2
        p = array([1 / 6, 2 / 3, 1 / 6])
    else:
        alpha = array([0, 1 / 2, 1 / 2, 1])
        beta[0, 0] = 1
        beta[1, 0] = 1 / 2
        beta[2, 1] = 1 / 2
        beta[3, 2] = 1
        p = array([1 / 6, 1 / 3, 1 / 3, 1 / 6])

    for i in range(n - 1):
        k = zeros((m, int(order)))

        for j in range(int(order)):
            k[:, j] = step * array(userfun(t[i] + alpha[j] * step, u[:, i] + beta[j, :] @ k.transpose()))

        u[:, i + 1] = u[:, i] + p @ k.transpose()

    return u
