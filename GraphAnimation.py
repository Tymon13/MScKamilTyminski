import copy
from tkinter import ttk

import matplotlib
import matplotlib.animation as ani
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ModelCalculator import ModelCalculator


class GraphAnimation:
    BUTTON_SIZE_PX = 25

    def __init__(self, tk_root: ttk.Frame, next_model: ModelCalculator):
        self.root = tk_root
        self.future_model = next_model
        self.current_model = copy.deepcopy(next_model)

        self.playback_buttons = self._make_playback_buttons()
        self.playback_buttons.grid(column=10, row=10)

        self.plot_widget = self._setup_plot()

        self.animator = None
        self.is_playing = False
        # self.start()  # TODO: to be removed when start/stop buttons will be there

    def _setup_plot(self):
        matplotlib.use('TkAgg')

        self.fig = plt.figure()
        self.fig.patch.set_color(str(ttk.Style().lookup('.', 'background')))
        plt.style.use('dark_background')

        self.ax = self.fig.add_subplot(111)
        self.ax.patch.set_alpha(0.0)
        self.ax.set(xlabel='x', ylabel='y')

        plot_widget = FigureCanvasTkAgg(self.fig, master=self.root)
        plot_widget.get_tk_widget().grid(column=10, row=20)

        return plot_widget

    def _make_playback_buttons(self):
        frame = ttk.Frame(self.root)

        self.play_icon = ImageTk.PhotoImage(
            Image.open('res/play_button.png').resize((self.BUTTON_SIZE_PX, self.BUTTON_SIZE_PX)))
        self.pause_icon = ImageTk.PhotoImage(
            Image.open('res/pause_button.png').resize((self.BUTTON_SIZE_PX, self.BUTTON_SIZE_PX)))
        self.stop_icon = ImageTk.PhotoImage(
            Image.open('res/stop_button.png').resize((self.BUTTON_SIZE_PX, self.BUTTON_SIZE_PX)))

        self.play_button = ttk.Button(frame, image=self.play_icon,
                                      command=lambda *args: self._play_button_callback(args))
        self.play_button.grid(column=10, row=10, padx=10, pady=10)

        self.stop_button = ttk.Button(frame, image=self.stop_icon,
                                      command=lambda *args: self._stop_button_callback(args))
        self.stop_button.grid(column=20, row=10, padx=10)

        return frame

    def _play_button_callback(self, *_):
        if not self.animator:
            self.play_button['image'] = self.pause_icon
            self.start()
            return

        if self.is_playing:
            self.play_button['image'] = self.play_icon
            self.pause()
        else:
            self.play_button['image'] = self.pause_icon
            self.resume()

    def _stop_button_callback(self, *_):
        self.play_button['image'] = self.play_icon
        self.stop()

    def start(self):
        self.current_model = copy.deepcopy(self.future_model)
        self.current_model.reset()
        self.is_playing = True

        self.plot_widget.get_tk_widget().destroy()
        self.plot_widget = self._setup_plot()

        self.animator = ani.FuncAnimation(self.fig, self._build_chart,
                                          frames=self.current_model.generate(self._stop_button_callback),
                                          init_func=lambda: None, interval=100, repeat=False)

    def _build_chart(self, frame_data):
        self.ax.stackplot(frame_data[0], frame_data[1], frame_data[2], frame_data[3],
                          labels=('Recovered', 'Infected', 'Susceptible'), colors=('blue', 'red', 'gray'))

    def stop(self):
        self.pause()
        self.animator = None

    def pause(self):
        if self.animator:
            self.is_playing = False
            self.animator.pause()

    def resume(self):
        if self.animator:
            self.is_playing = True
            self.animator.resume()
