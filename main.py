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
    p[0].set_color('white')
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
    fig.patch.set_color('#333333')
    ax = plt.axes()
    ax.patch.set_alpha(0.0)
    plt.ylabel('y')
    plt.xlabel('x')

    animator = ani.FuncAnimation(fig, build_chart, fargs=(x, y), save_count=len(x), interval=100)

    root = tk.Tk()
    root.tk.call("source", "themes/Azure-ttk-theme/azure.tcl")
    root.tk.call("set_theme", "dark")
    print(root['bg'])
    frame = ttk.Frame(root)
    frame.grid(column=1, row=0)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(column=0, row=1)

    options_frame = ttk.Frame(root)
    options_frame.grid(column=0, row=0)
    vaccination_switch = ttk.Checkbutton(options_frame, text='Vaccination', style='Switch.TCheckbutton', state='on')
    vaccination_switch.grid(column=0, row=0, columnspan=2)
    vaccination_delay_label = ttk.Label(options_frame, text='Days until vaccine is developed')
    vaccination_delay_label.grid(column=0, row=1)
    vaccination_delay = tk.IntVar(value=30)
    vaccination_delay_entry = ttk.Entry(options_frame, textvariable=vaccination_delay, width=3)
    vaccination_delay_entry.grid(column=1, row=1)

    vaccination_success_label = ttk.Label(options_frame, text='Chance of gaining immunity after vaccination (%)')
    vaccination_success_label.grid(column=0, row=2)
    vaccination_success = tk.IntVar(value=80)
    vaccination_success_entry = ttk.Entry(options_frame, textvariable=vaccination_success, width=3)
    vaccination_success_entry.grid(column=1, row=2)

    separator = ttk.Separator(options_frame, orient=tk.HORIZONTAL)
    separator.grid(column=0, row=3, columnspan=2, sticky=tk.EW)

    immunity_failure_switch = ttk.Checkbutton(options_frame, text='Immunity failure', style='Switch.TCheckbutton', state='on')
    immunity_failure_switch.grid(column=0, row=4, columnspan=2)

    immunity_failure_delay_label = ttk.Label(options_frame, text='Min days of immunity (until immunity can be lost)')
    immunity_failure_delay_label.grid(column=0, row=5)
    immunity_failure_delay = tk.IntVar(value=5)
    immunity_failure_delay_entry = ttk.Entry(options_frame, textvariable=immunity_failure_delay, width=3)
    immunity_failure_delay_entry.grid(column=1, row=5)

    immunity_failure_label = ttk.Label(options_frame, text='Chance of losing immunity (%)')
    immunity_failure_label.grid(column=0, row=6)
    immunity_failure = tk.IntVar(value=80)
    immunity_failure_entry = ttk.Entry(options_frame, textvariable=immunity_failure, width=3)
    immunity_failure_entry.grid(column=1, row=6)

    tk.mainloop()
