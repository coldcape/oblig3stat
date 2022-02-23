import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

lambda_t = float(input("λt: "))
x_limit = int(input("Øvrig grense for X: "))

x = np.arange(x_limit + 1)
stats.poisson.pmf(x, lambda_t)

plt.bar(x,stats.poisson.pmf(x, lambda_t))
plt.show()