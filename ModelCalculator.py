from typing import Callable

import numpy as np


class ModelCalculator:
    def __init__(self):
        self.frames = 1000
        self.population = 38_000_000
        self.R0 = 1.1
        self.recovery = 0.7

        self.vaccination_delay = 300
        self.vaccination_daily_percentage = 0.05
        self.vaccination_loss_delay = 180

        self.immunity_failure = 0.15

        self.x = None
        self.sus = None
        self.inf = None
        self.rec = None
        self.vac = None

        self.reset()

    def reset(self):
        self.x = np.arange(0, self.frames + 1)
        self.sus = np.zeros(self.frames + 1)
        self.inf = np.zeros(self.frames + 1)
        self.rec = np.zeros(self.frames + 1)
        self.vac = np.zeros(self.frames + 1)

    def generate(self, end_callback: Callable[[], None]):
        self.inf[0] = 1  # start the infection
        self.sus[0] = self.population - self.inf[0]
        for i in range(1, self.frames):
            # TODO: this assumes that (frames > recovery_time) and that all arrays are zeroes at the beginning
            new_infected = self.R0 * self.inf[i - 1] * self.sus[i - 1] / self.population
            new_infected = min(new_infected, self.sus[i - 1])
            new_recovered = self.inf[i - 1] * self.recovery
            new_recovered = max(new_recovered, 0)
            new_vaccinated = self.sus[i - 1] * self.vaccination_daily_percentage
            new_vaccinated = max(new_vaccinated, 0) if i > self.vaccination_delay else 0
            lost_immunity = self.rec[i - 1] * self.immunity_failure
            lost_vaccine = self.vac[i - self.vaccination_loss_delay] - self.vac[i - self.vaccination_loss_delay - 1]
            lost_vaccine = max(lost_vaccine, 0) if self.vaccination_loss_delay > 0 else 0

            self.sus[i] = self.sus[i - 1] - new_infected - new_vaccinated + lost_immunity + lost_vaccine
            self.inf[i] = self.inf[i - 1] + new_infected - new_recovered
            self.rec[i] = self.rec[i - 1] + new_recovered - lost_immunity
            self.vac[i] = self.vac[i - 1] + new_vaccinated - lost_vaccine

            yield self.x[:i], self.rec[:i], self.inf[:i], self.sus[:i], self.vac[:i]

        end_callback()
