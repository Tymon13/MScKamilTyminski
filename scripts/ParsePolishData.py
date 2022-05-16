import csv
import datetime
import os
import shutil
import tempfile


def get_cases_data(data_file, result):
    with tempfile.TemporaryDirectory() as temp_dir:
        shutil.unpack_archive(data_file, temp_dir)
        for filename in os.listdir(temp_dir):
            if not filename.endswith(".csv"):
                continue
            with open(os.path.join(temp_dir, filename)) as csvfile:
                dialect = csv.Sniffer().sniff(csvfile.read(2048), delimiters=";\n")
                csvfile.seek(0)
                reader = csv.DictReader(csvfile, dialect=dialect)
                for line in reader:
                    if line['wojewodztwo'] == 'Cały kraj':
                        if 'stan_rekordu_na' in line:
                            date = datetime.date.fromisoformat(line['stan_rekordu_na'])
                        else:
                            date = datetime.datetime.strptime(filename[:8], '%Y%m%d').date()

                        if date not in result:
                            result[date] = {}

                        if 'liczba_wszystkich_zakazen' in line:
                            result[date]['new_cases'] = int(line['liczba_wszystkich_zakazen'])
                        else:
                            result[date]['new_cases'] = int(line['liczba_przypadkow'])

                        if 'liczba_ozdrowiencow' in line:
                            result[date]['new_recovered'] = int(line['liczba_ozdrowiencow'])
                        else:
                            result[date]['new_recovered'] = 0

                        break
    return result


def get_cases_from_archival_data(data_file, result):
    with open(data_file) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(2048), delimiters=";\n")
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        for line in reader:
            date = datetime.datetime.strptime(line['Data'], '%d.%m.%Y').date()
            if date not in result:
                result[date] = {}
            result[date]['new_cases'] = int(line['Nowe przypadki'].replace(' ', ''))
            result[date]['new_recovered'] = int(line['Ozdrowieńcy (dzienna)'])
    return result


def get_vaccines_data(data_file, result):
    with tempfile.TemporaryDirectory() as temp_dir:
        shutil.unpack_archive(data_file, temp_dir)
        for filename in os.listdir(temp_dir):
            if not filename.endswith("global_szczepienia.csv"):
                continue
            with open(os.path.join(temp_dir, filename)) as csvfile:
                dialect = csv.Sniffer().sniff(csvfile.read(2048), delimiters=";\n")
                csvfile.seek(0)
                reader = csv.DictReader(csvfile, dialect=dialect)
                line = next(reader)
                date = datetime.datetime.strptime(filename[:8], '%Y%m%d').date()
                if date not in result:
                    result[date] = {}
                result[date]['new_vaccines'] = int(line['dawka_2_dziennie'])
    return result


def save_data(filename, data):
    with open(filename, mode='w+', newline='') as csvfile:
        new_data = []
        for date, content in data.items():
            new_data.append({'date': date, **content})
        new_data = sorted(new_data, key=lambda d: d['date'])
        writer = csv.DictWriter(csvfile, ['date', 'new_cases', 'new_recovered', 'new_vaccines'])
        writer.writeheader()
        writer.writerows(new_data)


if __name__ == '__main__':
    data = {}
    data = get_cases_data('../data/danehistorycznewojewodztwa.zip', data)
    data = get_cases_from_archival_data('../data/Zakazenia30323112020.csv', data)
    data = get_vaccines_data('../data/danehistoryczne_szczepienia.zip', data)
    save_data('../data/Polish_parsed.csv', data)
    # for key, value in data.items():
        # print(key, ":", value)
