import numpy as np


class ModelCalculator:
    def __init__(self):
        self.frames = 500
        self.population = 1000
        self.R0 = 2
        self.recovery_time = 5

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

    def generate(self):
        self.inf[0] = 1  # start the infection
        self.sus[0] = self.population - self.inf[0]
        for i in range(1, self.frames):
            # TODO: this assumes that (frames > recovery_time) and that all arrays are zeroes at the beginning
            new_infected = self.R0 * self.inf[i-1] * self.sus[i-1] / self.population
            new_infected = min(new_infected, self.sus[i-1])
            new_recovered = self.inf[i - self.recovery_time] - self.inf[i - self.recovery_time - 1]
            new_recovered = max(new_recovered, 0)

            self.sus[i] = self.sus[i-1] - new_infected
            self.inf[i] = self.inf[i-1] + new_infected - new_recovered
            self.rec[i] = self.rec[i-1] + new_recovered

            # self.sus[i] = self.sus[i-1] - self.R0
            # recovered = self.inf[i - self.recovery_time]
            # self.inf[i] = self.inf[i-1] * self.R0 - recovered
            # self.rec[i] = self.rec[i-1] + recovered
            yield self.x[:i+1], self.sus[:i+1], self.inf[:i+1], self.rec[:i+1]

    # def build_chart(self, frame_number: int, *args):
    #     self.sus = np.append(self.sus, [100 - frame_number * 2])
    #     self.inf = np.append(self.inf, [min(10, frame_number * 2)])
    #     self.rec = np.append(self.rec, [max((frame_number - 5) * 2, 0)])
    #     p_rec = plt.fill_between(np.arange(0, frame_number + 1), np.zeros(frame_number + 1), self.rec, color='gray')
    #     p_inf = plt.fill_between(np.arange(0, frame_number + 1), self.rec, self.rec + self.inf, color='red')
    #     p_sus = plt.fill_between(np.arange(0, frame_number + 1), self.rec + self.inf, self.rec + self.inf + self.sus,
    #                              color='blue')
    #     # p[0].set_color('white')
    #     # return p
