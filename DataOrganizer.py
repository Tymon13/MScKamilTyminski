import copy
import itertools

import numpy as np

from HistoricDataSupplier import HistoricDataSupplier
from ModelCalculator import ModelCalculator


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def concat(*iterables):
    for iterable in iterables:
        yield from iterable.generate()


class DataOrganizer:
    def __init__(self):
        self._settings_calculator = ModelCalculator()
        self._historic_data_supplier = HistoricDataSupplier("data/Polish_parsed.csv")

        self.current_model = None

    @property
    def settings(self):
        return self._settings_calculator

    @property
    def historic_data_suppplier(self):
        return self._historic_data_supplier

    def generate(self):
        self.current_model = copy.deepcopy(self._settings_calculator)
        self.current_model.reset()

        minima = self._historic_data_supplier.minima
        intervals = pairwise(minima)
        models = []
        for interval_begin, interval_end in intervals:
            model = copy.deepcopy(self.current_model)
            model.frames = interval_end - interval_begin
            model.start_from = interval_begin
            model.reset()
            models.append(model)

        simulations = []
        for model in models:
            *_, last = model.generate()
            simulations.append(last)

        final_simulation = [np.concatenate([sim[x] for sim in simulations]) for x in range(len(simulations[0]))]

        for index, historic_data in enumerate(self._historic_data_supplier.generate(), start=1):
            yield tuple(final_simulation[x][:index] for x in range(len(simulations[0]))), historic_data
        # for t in zip(self.current_model.generate(), self._historic_data_supplier.generate()):
        #     yield t
