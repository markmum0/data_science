# first the import
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#i used the plt.style.available to check available grid styles.
#print(plt.style.available)
# the method below implements the seaborn-v0_8-darkgrid style
plt.style.use('ggplot')
# then the first data set for all devs x and y-axis
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(age_x))
width = 0.25

dev_y = [5000, 6000, 4000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
# then the plot for all devs data including the color, line style,line thickness and the label
plt.bar(x_indexes-width, dev_y, width=width, color='k', linestyle='-', linewidth='2', label='All Devs')
# the y data set for python devs the x-axis will reuse the age data set
py_dev_y = [6540, 7500, 8400, 8700, 8980, 9100, 9350, 9540, 9645, 9880, 10100]
# plot command for the python data as well
plt.bar(x_indexes, py_dev_y, width=width, color='b', linestyle='--', linewidth='3', label='Python')
# the title of the graph with the x and y-axis labels
plt.title('Salaries for developers')
# makes adjustments on the x-axis
plt.xticks(ticks=x_indexes, labels=age_x)
# labeling axes
plt.xlabel('Ages')
plt.ylabel('Salaries (USD)')
# this shows a grid on the graph
plt.grid(True)
# it's the key
plt.legend()
# this shows the plot
plt.show()
