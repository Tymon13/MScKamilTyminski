from tkinter import ttk

import matplotlib
import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np


sus = np.zeros(0)
inf = np.zeros(0)
rec = np.zeros(0)


class GraphAnimation:
    def __init__(self, tk_root: ttk.Frame):
        x = np.arange(start=0, stop=100)
        y = np.arange(start=0, stop=100)

        matplotlib.use("TkAgg")

        fig = plt.figure()
        plt.style.use('dark_background')
        fig.patch.set_color(str(ttk.Style().lookup('.', 'background')))
        ax = plt.axes()
        ax.patch.set_alpha(0.0)
        plt.ylabel('y')
        plt.xlabel('x')

        canvas = FigureCanvasTkAgg(fig, master=tk_root)
        canvas.get_tk_widget().grid()

        self.animator = ani.FuncAnimation(fig, self.build_chart, frames=50, init_func=lambda: None, fargs=(x, y),
                                          interval=100, repeat=False)

    def build_chart(self, frame_number: int, *args):
        # x_, y_ = args
        global sus
        global inf
        global rec
        sus = np.append(sus, [100 - frame_number * 2])
        inf = np.append(inf, [min(10, frame_number * 2)])
        rec = np.append(rec, [max((frame_number - 5) * 2, 0)])
        p_rec = plt.fill_between(np.arange(0, frame_number + 1), np.zeros(frame_number + 1), rec, color='gray')
        p_inf = plt.fill_between(np.arange(0, frame_number + 1), rec, rec + inf, color='red')
        p_sus = plt.fill_between(np.arange(0, frame_number + 1), rec + inf, rec + inf + sus, color='blue')
        # p[0].set_color('white')
        # return p
