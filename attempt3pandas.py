import csv
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_response = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_response:
    language_counter.update(response.split(';'))

language = []
popularity = []

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])

plt.barh(language, popularity)

plt.title('Most Popular Languages')
plt.xlabel('No. of people who use')
plt.tight_layout()

plt.show()
