import csv


class HistoricDataSupplier:
    def __init__(self, filename):
        self.data = []

        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                self.data.append(line)

    def generate(self):
        for day in self.data:
            yield day
           