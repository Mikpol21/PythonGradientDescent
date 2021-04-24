import pandas as pd
import matplotlib.pyplot as plt
import Newton
import numpy as np
import loss_functions as loss
import time

zero = np.zeros(137)
F = loss.function1()
gd = Newton.GradientDescent(F)
number_of_I = 10

for type in ["Gradient", "Conjugate", "Newton"]:
    start = time.perf_counter()
    x = gd.Run(zero, type, number_of_I)
    end = time.perf_counter()
    print(type + "\n  Accuracy:\t" + str(F.good(x)*100) + "%\n  Time:\t" + str(round(end - start, 3)) + "sec")
    Graph = pd.read_csv("VacationProject/toPlot.csv", sep=";")
    if type == "Classic":
        L = "Gradient Descent"
    elif type == "N":
        L = "Newton's method"
    else:
        L = "Conjugate Descent"
    plt.plot(Graph.Iteration, Graph.Accuracy, label = L)


plt.title("Optimizing loss function")
plt.xlabel("Number of Iterations")
plt.ylabel("Accuracy")
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.legend()
plt.show()
