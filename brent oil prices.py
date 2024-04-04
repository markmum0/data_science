import csv
from collections import Counter

with open('BrentOilPrices.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

