import tkinter as tk
from tkinter import ttk

from ModelCalculator import ModelCalculator


class BaseOptions(ttk.Frame):
    def __init__(self, tk_root: ttk.Frame, model: ModelCalculator):
        super().__init__(tk_root)
        self.model = model

        self.days = tk.IntVar(value=self.model.frames)
        self.population = tk.IntVar(value=self.model.population)
        self.R0 = tk.DoubleVar(value=self.model.R0)
        self.recovery_time = tk.IntVar(value=self.model.recovery_time)

        self._setup_entry_callbacks()
        self._make_grid()

    def _make_grid(self):
        self.columnconfigure(10, weight=1)
        self.columnconfigure(20, weight=1)

        ttk.Label(master=self, text="Days of simulation").grid(column=10, row=10, sticky=tk.W)
        self.days_entry = ttk.Entry(master=self, textvariable=self.days, justify='right', width=3)
        self.days_entry.grid(column=20, row=10, sticky=tk.E)

        ttk.Label(master=self, text="Population").grid(column=10, row=20, sticky=tk.W)
        self.population_entry = ttk.Entry(master=self, textvariable=self.population, justify='right', width=6)
        self.population_entry.grid(column=20, row=20, sticky=tk.E)

        ttk.Label(master=self, text="R0").grid(column=10, row=30, sticky=tk.W)
        self.R0_entry = ttk.Entry(master=self, textvariable=self.R0, justify='right', width=3)
        self.R0_entry.grid(column=20, row=30, sticky=tk.E)

        ttk.Label(master=self, text="Recovery time (days)").grid(column=10, row=40, sticky=tk.W)
        self.recovery_entry = ttk.Entry(master=self, textvariable=self.recovery_time, justify='right', width=3)
        self.recovery_entry.grid(column=20, row=40, sticky=tk.E)

    def _setup_entry_callbacks(self):
        self.days.trace_add("write", lambda *_: setattr(self.model, "frames", self.days.get()))
        self.population.trace_add("write", lambda *_: setattr(self.model, "population", self.population.get()))
        self.R0.trace_add("write", lambda *_: setattr(self.model, "R0", self.R0.get()))
        self.recovery_time.trace_add("write", lambda *_: setattr(self.model, "recovery_time", self.recovery_time.get()))
