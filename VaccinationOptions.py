import tkinter as tk
from tkinter import ttk

from ModelCalculator import ModelCalculator


class VaccinationOptions(ttk.Frame):
    def __init__(self, tk_root: ttk.Frame, model: ModelCalculator):
        super().__init__(tk_root)
        self.model = model

        self.vaccination_on = tk.BooleanVar(value=False)
        self.vaccination_delay = tk.IntVar(value=self.model.vaccination_delay)
        self.vaccination_daily = tk.DoubleVar(value=self.model.vaccination_daily_percentage)
        self.sub_options = None

        self._setup_entry_callbacks()
        self._make_grid()

    def _make_grid(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        ttk.Label(self, text="Vaccination").grid(column=1, row=1, sticky=tk.W)
        self.vaccination_switch = ttk.Checkbutton(self, style='Switch.TCheckbutton', variable=self.vaccination_on)
        self.vaccination_switch.grid(column=2, row=1, sticky=tk.E)

        self._switch_sub_options()

    def _show_options(self):
        self.sub_options = ttk.Frame(self)
        self.sub_options.columnconfigure(1, weight=1)
        self.sub_options.columnconfigure(2, weight=1)

        ttk.Label(self.sub_options, text='Days before vaccine is developed').grid(column=1, row=1, sticky=tk.W)
        vaccination_delay_entry = ttk.Entry(self.sub_options, textvariable=self.vaccination_delay, width=3,
                                            justify='right')
        vaccination_delay_entry.grid(column=2, row=1, sticky=tk.E)

        ttk.Label(self.sub_options, text='Daily vaccinations').grid(column=1, row=2, sticky=tk.W)
        vaccination_daily_entry = ttk.Entry(self.sub_options, textvariable=self.vaccination_daily, width=4,
                                            justify='right')
        vaccination_daily_entry.grid(column=2, row=2, sticky=tk.E)

        self.model.vaccination_delay = self.vaccination_delay.get()
        self.model.vaccination_daily_percentage = self.vaccination_daily.get()
        self.sub_options.grid(column=1, row=2, columnspan=2, sticky=tk.EW)

    def _hide_options(self):
        if self.sub_options:
            self.sub_options.destroy()
        self.model.vaccination_delay = 0
        self.model.vaccination_daily_percentage = 0.0

    def _setup_entry_callbacks(self):
        self.vaccination_on.trace_add("write", self._switch_sub_options)
        self.vaccination_delay.trace_add(
            "write", lambda *_: setattr(self.model, "vaccination_delay", self.vaccination_delay.get()))
        self.vaccination_daily.trace_add(
            "write", lambda *_: setattr(self.model, "vaccination_daily_percentage", self.vaccination_daily.get()))

    def _switch_sub_options(self, *_):
        if self.vaccination_on.get():
            self._show_options()
        else:
            self._hide_options()
