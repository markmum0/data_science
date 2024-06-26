# first the import
import matplotlib
from matplotlib import pyplot as plt
#i used the plt.style.available to check available grid styles.
#print(plt.style.available)
# the method below implements the seaborn-v0_8-darkgrid style
plt.style.use('ggplot')
# then the first data set for all devs x and y-axis
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [5000, 6000, 4000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
# then the plot for all devs data including the color, line style,line thickness, marker style and the label
plt.plot(age_x, dev_y, color='k', linestyle='-', linewidth='2', marker='.', label='All Devs')
# the y data set for python devs the x-axis will reuse the age data set
py_dev_y = [6540, 7500, 8400, 8700, 8980, 9100, 9350, 9540, 9645, 9880, 10100]
# plot command for the python data as well
plt.plot(age_x, py_dev_y, color='b', linestyle='--', linewidth='3', marker='o', label='Python')
# the title of the graph with the x and y-axis labels
plt.title('Salaries for developers')
plt.xlabel('Ages')
plt.ylabel('Salaries (USD)')
# this shows a grid on the graph
plt.grid(True)
# its the key
plt.legend()
# this shows the plot
plt.show()
