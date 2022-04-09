import tkinter as tk
from tkinter import ttk

from BaseOptions import BaseOptions
from ImmunityFailureOptions import ImmunityFailureOptions
from ModelCalculator import ModelCalculator


def _make_vaccination_options_frame(root: ttk.Frame):
    vac_options = ttk.Frame(root)

    vaccination_switch = ttk.Checkbutton(vac_options, text='Vaccination', style='Switch.TCheckbutton', state='on')
    vaccination_switch.grid(column=0, row=0, columnspan=2)

    vaccination_delay_label = ttk.Label(vac_options, text='Days until vaccine is developed')
    vaccination_delay_label.grid(column=0, row=1)
    vaccination_delay = tk.IntVar(value=30)
    vaccination_delay_entry = ttk.Entry(vac_options, textvariable=vaccination_delay, width=3)
    vaccination_delay_entry.grid(column=1, row=1)

    vaccination_success_label = ttk.Label(vac_options, text='Chance of gaining immunity after vaccination (%)')
    vaccination_success_label.grid(column=0, row=2)
    vaccination_success = tk.IntVar(value=80)
    vaccination_success_entry = ttk.Entry(vac_options, textvariable=vaccination_success, width=3)
    vaccination_success_entry.grid(column=1, row=2)

    return vac_options


class OptionsFrame:
    def __init__(self, root: ttk.Frame, model: ModelCalculator):
        self.root = root
        self.model = model

        self.base_options = BaseOptions(self.root, self.model)
        self.base_options.grid(column=10, row=10, sticky=tk.EW)
        ttk.Separator(root, orient=tk.HORIZONTAL).grid(column=10, row=20, sticky=tk.EW)

        self.imm_failure_options = ImmunityFailureOptions(self.root, self.model)
        self.imm_failure_options.grid(column=10, row=30, sticky=tk.EW)
        ttk.Separator(root, orient=tk.HORIZONTAL).grid(column=10, row=40, sticky=tk.EW)

        # vac_options_frame = _make_vaccination_options_frame(self.root)
        # vac_options_frame.grid(column=10, row=30)
        # ttk.Separator(root, orient=tk.HORIZONTAL).grid(column=10, row=40, sticky=tk.EW)
