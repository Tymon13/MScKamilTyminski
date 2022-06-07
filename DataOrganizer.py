import copy

from HistoricDataSupplier import HistoricDataSupplier
from ModelCalculator import ModelCalculator


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
        for t in zip(self.current_model.generate(), self._historic_data_supplier.generate()):
            yield t
