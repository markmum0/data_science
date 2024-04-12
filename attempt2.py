import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('ggplot')

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('No. of people who use')
plt.tight_layout()

plt.show()