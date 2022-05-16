import csv

import numpy as np


class HistoricDataSupplier:
    def __init__(self, filename):
        self.data = []

        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                self.data.append(line)

    def generate(self):
        cases = np.zeros(len(self.data))
        vaccinated = np.zeros(len(self.data))
        for i in range(1, len(self.data)):
            new_cases = float(self.data[i]['new_cases']) if self.data[i]['new_cases'] else 0.0
            new_recovered = float(self.data[i]['new_recovered']) if self.data[i]['new_recovered'] else 0.0
            new_vaccines = float(self.data[i]['new_vaccines']) if self.data[i]['new_vaccines'] else 0.0

            cases[i] = cases[i - 1] + new_cases - new_recovered
            vaccinated[i] = vaccinated[i - 1] + new_vaccines

            yield cases[:i], vaccinated[:i]
