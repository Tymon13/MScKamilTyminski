import copy
from tkinter import ttk

import matplotlib
import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ModelCalculator import ModelCalculator


class GraphAnimation:
    def __init__(self, tk_root: ttk.Frame, next_model: ModelCalculator):
        self.root = tk_root
        self.future_model = next_model
        self.current_model = copy.deepcopy(next_model)

        self._setup_plot()

        self.animator = None
        self.start()  # TODO: to be removed when start/stop buttons will be there

    def _setup_plot(self):
        matplotlib.use('TkAgg')

        self.fig = plt.figure()
        self.fig.patch.set_color(str(ttk.Style().lookup('.', 'background')))
        plt.style.use('dark_background')

        self.ax = self.fig.add_subplot(111)
        self.ax.patch.set_alpha(0.0)
        self.ax.set(xlabel='x', ylabel='y')

        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().grid()

    def start(self):
        self.current_model = copy.deepcopy(self.future_model)
        self.current_model.reset()
        self.animator = ani.FuncAnimation(self.fig, self._build_chart, frames=self.current_model.generate(),
                                          init_func=lambda: None, interval=100, repeat=False)

    def _build_chart(self, frame_data):
        self.ax.stackplot(frame_data[0], frame_data[1], frame_data[2], frame_data[3],
                          labels=('Susceptible', 'Infected', 'Recovered'), colors=('gray', 'red', 'blue'))

    def stop(self):
        self.animator = None

    def pause(self):
        if self.animator:
            self.animator.pause()

    def resume(self):
        if self.animator:
            self.animator.resume()
