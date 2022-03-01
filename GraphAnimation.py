from tkinter import ttk

import matplotlib
import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ModelCalculator import ModelCalculator


class GraphAnimation:
    def __init__(self, tk_root: ttk.Frame, model: ModelCalculator):
        self.root = tk_root
        self.model = model

        matplotlib.use('TkAgg')

        fig = plt.figure()
        plt.style.use('dark_background')
        fig.patch.set_color(str(ttk.Style().lookup('.', 'background')))
        ax = plt.axes()
        ax.patch.set_alpha(0.0)
        plt.ylabel('y')
        plt.xlabel('x')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().grid()

        self.animator = ani.FuncAnimation(fig, self.model.build_chart, frames=50, init_func=lambda: None, interval=100,
                                          repeat=False)
