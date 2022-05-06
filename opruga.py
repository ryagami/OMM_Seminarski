import numpy as np
import matplotlib.pyplot as plt
# import time

import animation as anim
import GUI


def opruga_rk(c, k, l, f, a, b, t_range, step, m):  # tol, ind):
    # c, k, l i f su kao iz zadatka
    # a i b su alfa i beta
    # [0, xrange] je interval na kojem racunamo vrednosti sa korakom h
    # m je red metode, tol je preciznost
    # ind je indikator da li zelimo modifikovanu RK metodu

    def fu(t1, u1, v1):
        return v1

    def fv(t1, u1, v1):
        return f(t1) - c * v1 - k * u1 - l * pow(u1, 3)

    t = np.arange(0, t_range + step, step)
    n = len(t)

    u = np.zeros(n)
    u[0] = a
    v = np.zeros(n)
    v[0] = b

    beta = np.zeros((int(m), int(m)))

    # izbor reda Runge-Kutta metode
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

    # print(beta)

    for i in range(n - 1):
        ku = np.zeros(int(m))
        kv = np.zeros(int(m))

        for j in range(int(m)):
            ku[j] = step * fu(t[i] + alpha[j] * step, u[i] + beta[j, :] @ ku, v[i] + beta[j, :] @ ku.transpose())
            kv[j] = step * fv(t[i] + alpha[j] * step, u[i] + beta[j, :] @ kv, v[i] + beta[j, :] @ kv.transpose())

        u[i + 1] = u[i] + p @ ku
        v[i + 1] = v[i] + p @ kv

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
    fig.tight_layout()

    ax1.plot(t, u)
    ax1.set_title("Grafik funkcije položaja")
    ax1.set_xlabel("t")
    ax1.set_ylabel("x")

    ax2.plot(t, v)
    ax2.set_title("Grafik funkcije brzine")
    ax2.set_xlabel("t")
    ax2.set_ylabel("x'")

    ax3.plot(u, v)
    ax3.set_title("Fazni grafik")
    ax3.set_xlabel("x")
    ax3.set_ylabel("x'")

    ax4.plot(t, fv(t, u, v))
    ax4.set_title("Grafik ubrzanja")
    ax4.set_xlabel("t")
    ax4.set_ylabel("x''")

    # plt.show()

    o = {
        "range": t,
        "position": u,
        "speed": v,
        "acceleration": fv(t, u, v)
    }

    return o


if __name__ == '__main__':
    def f(t):
        return -9.81


    o = opruga_rk(0.0, 0.3, 0.04, f, 1.0, 0.0, 40, 0.001, 4)
    anim.animate(o, 30)
