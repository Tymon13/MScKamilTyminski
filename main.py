import tkinter as tk
from tkinter import ttk

from GraphAnimation import GraphAnimation
from OptionsFrame import OptionsFrame

if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call('source', 'themes/Azure-ttk-theme/azure.tcl')
    root.tk.call('set_theme', 'dark')

    graph_frame = ttk.Frame(root)
    graph_frame.grid(column=1, row=0)
    graph = GraphAnimation(graph_frame)

    options_frame = ttk.Frame(root)
    options_frame.grid(column=0, row=0)
    options = OptionsFrame(options_frame)

    root.protocol('WM_DELETE_WINDOW', lambda: root.quit())
    tk.mainloop()
