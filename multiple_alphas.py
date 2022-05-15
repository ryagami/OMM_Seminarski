import numpy as np
import matplotlib.pyplot as plt

import opruga
import period

c = 0
f = '0'
k = 0.3
j = 0.004
beta = 0
t_range = 90
alfas = np.arange(0.5, 3, 0.5)

def grafik_polozaja():
    for alfa in alfas:
        o = opruga.opruga_rk(c, k, j, f, alfa, beta, t_range, 0.001, 4)
        plt.plot(o['range'], o['position'], label = f"alfa = {alfa}")
        
    plt.xlabel("vreme")
    plt.ylabel("polozaj")
    plt.title("Grafik polozaja")
    plt.legend(loc='upper right', fontsize = 'small')
    plt.show()

def grafik_brzine():
    for alfa in alfas:
        o = opruga.opruga_rk(c, k, j, f, alfa, beta, t_range, 0.001, 4)
        plt.plot(o['range'], o['speed'], label = f"alfa = {alfa}")
        
    plt.xlabel("vreme")
    plt.ylabel("brzina")
    plt.title("Grafik brzine")
    plt.legend(loc='upper right', fontsize = 'small')
    plt.show()

def fazni_grafik():
    for alfa in alfas:
        o = opruga.opruga_rk(c, k, j, f, alfa, beta, t_range, 0.001, 4)
        plt.plot(o['position'], o['speed'], label = f"alfa = {alfa}")
        
    plt.xlabel("polozaj")
    plt.ylabel("brzina")
    plt.title("Fazni grafik")
    plt.legend(loc='upper right', fontsize = 'small')
    plt.show()

def main():
    grafik_polozaja()
    # grafik_brzine()
    # fazni_grafik()

if __name__ == "__main__":
    main()