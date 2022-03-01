import matplotlib.pyplot as plt
import numpy as np


class ModelCalculator:
    def __init__(self):
        self.sus = np.zeros(0)
        self.inf = np.zeros(0)
        self.rec = np.zeros(0)

    def build_chart(self, frame_number: int, *args):
        self.sus = np.append(self.sus, [100 - frame_number * 2])
        self.inf = np.append(self.inf, [min(10, frame_number * 2)])
        self.rec = np.append(self.rec, [max((frame_number - 5) * 2, 0)])
        p_rec = plt.fill_between(np.arange(0, frame_number + 1), np.zeros(frame_number + 1), self.rec, color='gray')
        p_inf = plt.fill_between(np.arange(0, frame_number + 1), self.rec, self.rec + self.inf, color='red')
        p_sus = plt.fill_between(np.arange(0, frame_number + 1), self.rec + self.inf, self.rec + self.inf + self.sus,
                                 color='blue')
        # p[0].set_color('white')
        # return p
