import tkinter as tk
from tkinter import ttk

from GraphAnimation import GraphAnimation
from ModelCalculator import ModelCalculator
from OptionsFrame import OptionsFrame


class App:
    def __init__(self, tk_root: tk.Tk):
        self.root = tk_root
        self.set_dark_theme()
        self.set_graceful_exit_on_window_close()
        self.model = ModelCalculator()

        graph_frame = ttk.Frame(tk_root)
        graph_frame.grid(column=1, row=0)
        self.graph = GraphAnimation(graph_frame, self.model)

        options_frame = ttk.Frame(tk_root)
        options_frame.grid(column=0, row=0)
        self.options = OptionsFrame(options_frame, self.model)

    def set_graceful_exit_on_window_close(self):
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.root.quit())

    def set_dark_theme(self):
        self.root.tk.call('source', 'themes/Azure-ttk-theme/azure.tcl')
        self.root.tk.call('set_theme', 'dark')
