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
        self.model.reset()

        matplotlib.use('TkAgg')

        self.fig = plt.figure()
        self.fig.patch.set_color(str(ttk.Style().lookup('.', 'background')))
        plt.style.use('dark_background')

        self.ax = self.fig.add_subplot(111)
        self.ax.patch.set_alpha(0.0)
        self.ax.set(xlabel='x', ylabel='y')

        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().grid()

        self.animator = ani.FuncAnimation(self.fig, self.build_chart, frames=self.model.generate(),
                                          init_func=lambda: None, interval=100, repeat=False)

    def build_chart(self, frame_data):
        self.ax.stackplot(frame_data[0], frame_data[1], frame_data[2], frame_data[3],
                          labels=('Susceptible', 'Infected', 'Recovered'), colors=('gray', 'red', 'blue'))
