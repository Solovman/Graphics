import matplotlib.pyplot as plt
import numpy as np

# Random distribution graph
np.random.seed(123456789)
mu = 100
sigma = 15
x = sigma + mu + np.random.randn(478)

num_bins = 50

fig, ax = plt.subplots()

n, bins, patches, = ax.hist(x, num_bins, density=True)

plt.show()
