# first the import
import csv
from collections import Counter
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
# the method below implements the seaborn-v0_8-darkgrid style
plt.style.use('ggplot')
#opening the data.csv file
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# using the counter function from collections to count the frequency of the languages used.
    language_counter = Counter()
# looping through the csv file
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

print(language_counter.most_common(15))
#plt.title('Salaries for developers')
#plt.xlabel('Ages')
#plt.ylabel('Salaries (USD)')
# this shows a grid on the graph
#plt.grid(True)
# its the key
#plt.legend()
# this shows the plot
#plt.show()
