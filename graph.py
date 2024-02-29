from matplotlib.pyplot import *
import numpy as np

# Function graph sin(x/2) * e^x
x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(x / 2) * np.e ** x
plot(x, y)
grid()
show()
