import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

forventnings_verdi = 760
standard_avvik = 10

x = int(input("Vekt av brød: "))

y = stats.norm.cdf(x = x, loc = forventnings_verdi, scale = standard_avvik)


print(1 - y)