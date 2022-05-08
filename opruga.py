import sys
from numpy import *
import matplotlib.pyplot as plt
from io import StringIO
from contextlib import redirect_stdout

import animation as anim

set_printoptions(threshold=sys.maxsize)


def opruga_rk(c, k, l, f, a, b, t_range, step, m):  # tol, ind):
    # c, k, l i f su kao iz zadatka
    # a i b su alfa i beta
    # [0, xrange] je interval na kojem racunamo vrednosti sa korakom h
    # m je red metode, tol je preciznost
    # ind je indikator da li zelimo modifikovanu RK metodu

    # Solves the system u' = fu(t, u, v), v' = fv(t, u, v)

    def fu(t, u, v):
        return v

    # Executes the input string f as python code and prints the result into out to grab the value
    def fv(t, u, v):
        out = StringIO()
        with redirect_stdout(out):
            exec("print(" + f + ")")
            return float(out.getvalue()) - c * v - k * u - l * pow(u, 3)

    t = arange(0, t_range + step, step)
    n = len(t)

    u = zeros(n)
    u[0] = a
    v = zeros(n)
    v[0] = b

    beta = zeros((int(m), int(m)))

    # Choosing Runge-Kutta method order
    if m == 1:
            alpha = 0
            beta = 1
            p = 1
    elif m == 2:
            alpha = array([0, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1
            p = array([1 / 2, 1 / 2])
    elif m == 2.1:
            alpha = array([0, 1 / 2])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            p = array([0, 1])
    elif m == 3:
            alpha = array([0, 1 / 2, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            beta[2, 0] = -1
            beta[2, 1] = 2
            p = array([1 / 6, 2 / 3, 1 / 6])
    else :
            alpha = array([0, 1 / 2, 1 / 2, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            beta[2, 1] = 1 / 2
            beta[3, 2] = 1
            p = array([1 / 6, 1 / 3, 1 / 3, 1 / 6])

    for i in range(n - 1):
        ku = zeros(int(m))
        kv = zeros(int(m))

        for j in range(int(m)):
            ku[j] = step * fu(t[i] + alpha[j] * step, u[i] + beta[j, :] @ ku, v[i] + beta[j, :] @ ku.transpose())
            kv[j] = step * fv(t[i] + alpha[j] * step, u[i] + beta[j, :] @ kv, v[i] + beta[j, :] @ kv.transpose())

        u[i + 1] = u[i] + p @ ku
        v[i + 1] = v[i] + p @ kv

    o = {
        "range": t,
        "position": u,
        "speed": v,
        "acceleration": list(map(fv, t, u, v))
    }

    return o
