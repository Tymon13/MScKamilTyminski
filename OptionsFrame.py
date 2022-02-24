import tkinter as tk
from tkinter import ttk


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


def _make_immunity_failure_options(root: ttk.Frame):
    imm_fail_frame = ttk.Frame(root)
    immunity_failure_switch = ttk.Checkbutton(imm_fail_frame, text='Immunity failure', style='Switch.TCheckbutton',
                                              state='on')
    immunity_failure_switch.grid(column=0, row=4, columnspan=2)

    immunity_failure_delay_label = ttk.Label(imm_fail_frame,
                                             text='Min days of immunity (until immunity can be lost)')
    immunity_failure_delay_label.grid(column=0, row=5)
    immunity_failure_delay = tk.IntVar(value=5)
    immunity_failure_delay_entry = ttk.Entry(imm_fail_frame, textvariable=immunity_failure_delay, width=3)
    immunity_failure_delay_entry.grid(column=1, row=5)

    immunity_failure_label = ttk.Label(imm_fail_frame, text='Chance of losing immunity (%)')
    immunity_failure_label.grid(column=0, row=6)
    immunity_failure = tk.IntVar(value=80)
    immunity_failure_entry = ttk.Entry(imm_fail_frame, textvariable=immunity_failure, width=3)
    immunity_failure_entry.grid(column=1, row=6)

    return imm_fail_frame


class OptionsFrame:
    def __init__(self, root: ttk.Frame):
        self.root = root
        vac_options_frame = _make_vaccination_options_frame(self.root)
        vac_options_frame.grid(column=0, row=0)

        separator = ttk.Separator(root, orient=tk.HORIZONTAL)
        separator.grid(column=0, row=3, columnspan=2, sticky=tk.EW)

        immunity_failure_frame = _make_immunity_failure_options(self.root)
        immunity_failure_frame.grid(column=0, row=20)
