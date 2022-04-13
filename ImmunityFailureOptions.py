import tkinter as tk
from tkinter import ttk

from ModelCalculator import ModelCalculator


class ImmunityFailureOptions(ttk.Frame):
    def __init__(self, tk_root: ttk.Frame, model: ModelCalculator):
        super().__init__(tk_root)
        self.model = model

        self.immunity_failure_on = tk.BooleanVar(value=False)
        self.immunity_failure_chance = tk.DoubleVar(value=self.model.immunity_failure)
        self.sub_options = None

        self._setup_entry_callbacks()
        self._make_grid()

    def _make_grid(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        ttk.Label(self, text="Immunity failure").grid(column=1, row=1, sticky=tk.W)
        self.immunity_failure_switch = ttk.Checkbutton(self, style='Switch.TCheckbutton',
                                                       variable=self.immunity_failure_on)
        self.immunity_failure_switch.grid(column=2, row=1, sticky=tk.E)

        self._switch_sub_options()

    def _show_options(self):
        self.sub_options = ttk.Frame(self)
        self.sub_options.columnconfigure(1, weight=1)
        self.sub_options.columnconfigure(2, weight=1)

        ttk.Label(self.sub_options, text='Chance of losing immunity').grid(column=1, row=1, sticky=tk.W)
        immunity_failure_entry = ttk.Entry(self.sub_options, textvariable=self.immunity_failure_chance, width=4,
                                           justify='right')
        immunity_failure_entry.grid(column=2, row=1, sticky=tk.E)
        self.sub_options.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
        self.model.immunity_failure = self.immunity_failure_chance.get()

    def _hide_options(self):
        if self.sub_options:
            self.sub_options.destroy()
        self.model.immunity_failure = 0

    def _setup_entry_callbacks(self):
        self.immunity_failure_on.trace_add("write", self._switch_sub_options)
        self.immunity_failure_chance.trace_add(
            "write", lambda *_: setattr(self.model, "immunity_failure", self.immunity_failure_chance.get()))

    def _switch_sub_options(self, *_):
        if self.immunity_failure_on.get():
            self._show_options()
        else:
            self._hide_options()
