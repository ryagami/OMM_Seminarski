import numpy as np
import matplotlib.pyplot as plt
# import time


def opruga_rk(c, k, j, f, a, b, M, h, m, tol, ind):
    def fu(t, u, v):
        return v

    def fv(t, u, v):
        return f(t) - c * v - k * u - j * pow(u, 3)

    t = np.arange(0, M + h, h)
    n = len(t)

    u = np.zeros(n)
    u[0] = a
    v = np.zeros(n)
    v[0] = b

    beta = np.zeros((m, m))

    match m:
        case 1:
            alpha = 0
            beta = 1
            p = 1
        case 2:
            alpha = np.array([0, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1
            p = np.array([1 / 2, 1 / 2])
        case 2.1:
            alpha = np.array([0, 1 / 2])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            p = np.array([0, 1])
        case 3:
            alpha = np.array([0, 1 / 2, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            beta[2, 0] = -1
            beta[2, 1] = 2
            p = np.array([1 / 6, 2 / 3, 1 / 6])
        case _:
            alpha = np.array([0, 1 / 2, 1 / 2, 1])
            beta[0, 0] = 1
            beta[1, 0] = 1 / 2
            beta[2, 1] = 1 / 2
            beta[3, 2] = 1
            p = np.array([1 / 6, 1 / 3, 1 / 3, 1 / 6])

    print(beta)

    for i in range(0, n - 1):
        ku = np.zeros(m)
        kv = np.zeros(m)

        for j in range(0, m):
            ku[j] = h * fu(t[i] + alpha[j] * h, u[i] + beta[j, :] @ ku, v[i] + beta[j, :] @ ku.transpose())
            kv[j] = h * fv(t[i] + alpha[j] * h, u[i] + beta[j, :] @ kv, v[i] + beta[j, :] @ kv.transpose())

        u[i + 1] = u[i] + p @ ku
        v[i + 1] = v[i] + p @ kv

    plt.plot(t, u)
    plt.show()


if __name__ == '__main__':
    def f(t):
        return 0

    opruga_rk(0.0, 0.3, 0.04, f, 0.1, 0.0, 1000.0, 0.001, 4, 0.001, 0)
