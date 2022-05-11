from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np

import opruga
import period

matplotlib.use("TkAgg")

if __name__ == '__main__':
    root = Tk()
    root.title("Grafici oscilacije jake opruge")
    root.columnconfigure((1, 3, 5), weight=1)
    root.rowconfigure(4, weight=1)


    def onCLick_plot():
        c = entry_c.get()
        k = entry_k.get()
        j = entry_j.get()
        f = entry_f.get()
        alpha = entry_alpha.get()
        beta = entry_beta.get()
        t_range = entry_trange.get()
        c = float(c) if c != "" else 0.0
        k = float(k) if k != "" else 0.0
        j = float(j) if j != "" else 0.0
        f = f if f != "" else "0"
        alpha = float(alpha) if alpha != "" else 0.0
        beta = float(beta) if beta != "" else 0.0
        t_range = float(t_range) if t_range != "" else 0.0

        tickEraseValue = askyesno("Erase canvas", "Do you want to clear canvases?")
        # If above is "yes", clear all figure subplots and make new ones

        o = opruga.opruga_rk(c, k, j, f, alpha, beta, t_range, 0.001, 4)
        p = period.period_array(k, j, 60, 0.001)

        fig4.clear()
        # global anim_plot
        anim_plot = fig4.add_subplot(111)

        if tickEraseValue:
            fig1.clear()
            global plot1
            plot1 = fig1.add_subplot(111)
            fig2.clear()
            global plot2
            plot2 = fig2.add_subplot(111)
            fig3.clear()
            global plot3
            plot3 = fig3.add_subplot(111)
            fig5.clear()
            global plot5
            plot5 = fig5.add_subplot(111)

        plot1.plot(o["range"], o["position"])
        canvas1.draw()

        plot2.plot(o["range"], o["speed"])
        canvas2.draw()

        plot3.plot(o["position"], o["speed"])
        canvas3.draw()

        def animate(i):
            spring.set_ydata(o["position"][50*i])
            return spring,

        anim_plot.set_ylim([min(o["position"])-0.1, max(o["position"])+0.1])
        spring, = anim_plot.plot(o["range"][-1]/2, o["position"][0], 'ro', markersize=10)
        global anim
        anim = animation.FuncAnimation(fig4, animate, int(len(o["range"])/50), interval=25, blit=False)

        plot5.plot(p['alpha'], p['period'])
        plot5.plot(alpha, period.period(k, j, alpha), 'go', markersize=5)
        canvas5.draw()

    #############################################
    #                                           #
    #        Entry fields for parameters        #
    #                                           #
    #############################################

    label_c = ttk.Label(root, text="c")
    label_c.grid(row=0, column=0)
    entry_c = ttk.Entry(root)
    entry_c.grid(row=0, column=1, padx=5, pady=5, sticky=W + E)
    entry_c.insert(0, "0")

    label_k = ttk.Label(root, text="k")
    label_k.grid(row=0, column=2)
    entry_k = ttk.Entry(root)
    entry_k.grid(row=0, column=3, padx=5, pady=5, sticky=W + E)
    entry_k.insert(0, "0.3")

    label_j = ttk.Label(root, text="j")
    label_j.grid(row=0, column=4)
    entry_j = ttk.Entry(root)
    entry_j.grid(row=0, column=5, padx=5, pady=5, sticky=W + E)
    entry_j.insert(0, "0.04")

    label_f = ttk.Label(root, text="f(t)")
    label_f.grid(row=1, column=0)
    entry_f = ttk.Entry(root)
    entry_f.grid(row=1, column=1, padx=5, pady=5, sticky=W + E)
    entry_f.insert(0, "0")

    label_alpha = ttk.Label(root, text="alpha")
    label_alpha.grid(row=1, column=2)
    entry_alpha = ttk.Entry(root)
    entry_alpha.grid(row=1, column=3, padx=5, pady=5, sticky=W + E)
    entry_alpha.insert(0, "0.1")

    label_beta = ttk.Label(root, text="beta")
    label_beta.grid(row=1, column=4)
    entry_beta = ttk.Entry(root)
    entry_beta.grid(row=1, column=5, padx=5, pady=5, sticky=W + E)
    entry_beta.insert(0, "0")
    
    label_trange = ttk.Label(root, text="range")
    label_trange.grid(row=2, column=0)
    entry_trange = ttk.Entry(root)
    entry_trange.grid(row=2, column=1, padx=5, pady=5, sticky=W + E)
    entry_trange.insert(0, "30")

    button_plot = ttk.Button(root, text="Nacrtaj", command=onCLick_plot)
    button_plot.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

    ####################################################
    #                                                  #
    #        Function plots separated into tabs        #
    #                                                  #
    ####################################################

    plot_tabs = ttk.Notebook(root)

    plot_tab1 = ttk.Frame(plot_tabs)
    plot_tabs.add(plot_tab1, text="Grafik položaja", sticky="news")
    plot_tab1.columnconfigure(0, weight=1)
    fig1 = Figure(figsize=(5, 5), dpi=100)
    canvas1 = FigureCanvasTkAgg(fig1, plot_tab1)
    plot1 = fig1.add_subplot(111)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)# grid(row=0, column=0, sticky="news")

    plot_tab2 = ttk.Frame(plot_tabs)
    plot_tabs.add(plot_tab2, text="Grafik brzine", sticky="news")
    plot_tab2.columnconfigure(0, weight=1)
    fig2 = Figure(figsize=(5, 5), dpi=100)
    canvas2 = FigureCanvasTkAgg(fig2, plot_tab2)
    plot2 = fig2.add_subplot(111)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)# grid(row=0, column=0, sticky="news")

    plot_tab3 = ttk.Frame(plot_tabs)
    plot_tabs.add(plot_tab3, text="Fazni grafik", sticky="news")
    plot_tab3.columnconfigure(0, weight=1)
    fig3 = Figure(figsize=(5, 5), dpi=100)
    canvas3 = FigureCanvasTkAgg(fig3, plot_tab3)
    plot3 = fig3.add_subplot(111)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)# grid(row=0, column=0, sticky=W+E)

    plot_tab4 = ttk.Frame(plot_tabs)
    plot_tabs.add(plot_tab4, text="Animacija", sticky="news")
    plot_tab4.columnconfigure(0, weight=1)
    fig4 = Figure(figsize=(5, 5), dpi=100)
    canvas4 = FigureCanvasTkAgg(fig4, plot_tab4)
    canvas4.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    anim_plot = fig4.add_subplot(111)

    plot_tab5 = ttk.Frame(plot_tabs)
    plot_tabs.add(plot_tab5, text="Period", sticky="news")
    plot_tab5.columnconfigure(0, weight=1)
    fig5 = Figure(figsize=(5, 5), dpi=100)
    canvas5 = FigureCanvasTkAgg(fig5, plot_tab5)
    plot5 = fig5.add_subplot(111)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    global spring
    global anim

    plot_tabs.grid(row=5, column=0, columnspan=6, sticky="news")

    # tickEraseValue = IntVar()
    # tickEraseCanvas = ttk.Checkbutton(root, text="Erase canvases before drawing?", variable=tickEraseValue)
    # tickEraseCanvas.grid(row=5, column=0, columnspan=6, sticky="w")

    root.mainloop()
