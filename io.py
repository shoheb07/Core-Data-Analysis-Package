import csv
from .dataframe import DataFrame

def read_csv(filename):
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return DataFrame(data)
