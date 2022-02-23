import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

forventnings_verdi = 760
standard_avvik = 10


x = np.arange(720, 800 + 1)

y = stats.norm.pdf(x = x, loc = forventnings_verdi, scale = standard_avvik)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Normalfordeling")


plt.show()
