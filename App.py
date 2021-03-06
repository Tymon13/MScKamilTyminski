import tkinter as tk
from tkinter import ttk

from DataOrganizer import DataOrganizer
from GraphAnimation import GraphAnimation
from OptionsFrame import OptionsFrame


class App:
    def __init__(self, tk_root: tk.Tk):
        self.root = tk_root
        self.set_dark_theme()
        self.set_graceful_exit_on_window_close()
        self.data_organizer = DataOrganizer()

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        graph_frame = ttk.Frame(tk_root)
        graph_frame.grid(column=1, row=0, sticky=tk.NSEW)
        self.graph = GraphAnimation(graph_frame, self.data_organizer)

        options_frame = ttk.Frame(tk_root)
        options_frame.grid(column=0, row=0)
        self.options = OptionsFrame(options_frame, self.data_organizer.settings)

    def set_graceful_exit_on_window_close(self):
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.root.quit())

    def set_dark_theme(self):
        self.root.tk.call('source', 'themes/Azure-ttk-theme/azure.tcl')
        self.root.tk.call('set_theme', 'dark')
