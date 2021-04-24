"""import pandas as pd
import matplotlib.pyplot as plt

Graph = pd.read_csv("VacationProject/toPlot.csv", sep=";")
Graph
plt.hist(Graph.Iteration)
plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

# X axis parameter:
xaxis = np.array([2, 8])

# Y axis parameter:
yaxis = np.array([4, 9])

plt.plot(xaxis, yaxis)
plt.show()
