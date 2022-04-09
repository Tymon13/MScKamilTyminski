from typing import Callable

import numpy as np


class ModelCalculator:
    def __init__(self):
        self.frames = 100
        self.population = 1000
        self.R0 = 2
        self.recovery = 0.7

        self.immunity_failure = 0.15

        self.x = None
        self.sus = None
        self.inf = None
        self.rec = None

        self.reset()

    def reset(self):
        self.x = np.arange(0, self.frames)
        self.sus = np.zeros(self.frames)
        self.inf = np.zeros(self.frames)
        self.rec = np.zeros(self.frames)

    def generate(self, end_callback: Callable[[], None]):
        self.inf[0] = 1  # start the infection
        self.sus[0] = self.population - self.inf[0]
        for i in range(1, self.frames):
            # TODO: this assumes that (frames > recovery_time) and that all arrays are zeroes at the beginning
            new_infected = self.R0 * self.inf[i - 1] * self.sus[i - 1] / self.population
            new_infected = min(new_infected, self.sus[i - 1])
            new_recovered = self.inf[i - 1] * self.recovery
            new_recovered = max(new_recovered, 0)
            lost_immunity = self.rec[i - 1] * self.immunity_failure

            self.sus[i] = self.sus[i - 1] - new_infected + lost_immunity
            self.inf[i] = self.inf[i - 1] + new_infected - new_recovered
            self.rec[i] = self.rec[i - 1] + new_recovered - lost_immunity

            yield self.x[:i + 1], self.rec[:i + 1], self.inf[:i + 1], self.sus[:i + 1]

        end_callback()
