# first the import
import csv
from collections import Counter
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
# the method below implements the seaborn-v0_8-darkgrid style
plt.style.use('ggplot')
#opening the data.csv file
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# using the counter function from collections to count the frequency of the languages used.
    language_counter = Counter()
# looping through the csv file
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common():
    languages.append(item[0])
    popularity.append(item[1])

plt.barh(languages, popularity)
plt.title('Most Used Languages')
plt.xlabel('Popularity')
plt.ylabel('Languages')
# this shows a grid on the graph
plt.grid(True)
# its the key
#plt.legend()
# this shows the plot
plt.show()
