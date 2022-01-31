import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np


def build_chart(frame_number: int, *args):
    x_, y_ = args
    p = plt.plot(x_[:frame_number], y_[:frame_number])
    p[0].set_color('black')
    if frame_number == 50:
        animator.pause()
        import time
        time.sleep(2)
        animator.resume()
    return p


if __name__ == '__main__':
    x = np.arange(start=0, stop=100)
    y = np.arange(start=0, stop=100)

    matplotlib.use("TkAgg")

    fig = plt.figure()
    plt.ylabel('y')
    plt.xlabel('x')

    animator = ani.FuncAnimation(fig, build_chart, fargs=(x, y), save_count=len(x), interval=100)

    root = tk.Tk()
    root.tk.call("source", "themes/Azure-ttk-theme/azure.tcl")
    root.tk.call("set_theme", "dark")
    frame = ttk.Frame(root)
    frame.grid(column=0, row=0)
    label = ttk.Label(frame, text='Hello World!')
    label.grid(column=0, row=0)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(column=0, row=1)
    tk.mainloop()
