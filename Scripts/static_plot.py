# STATIC PLOT

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import subprocess as sp

x = np.load('x_data.npy')
y = np.load('y_data.npy')

fig = plt.figure()
fig.canvas.manager.set_window_title('Frequency Spectrum')
fig.subplots_adjust(bottom=0.15)
line, = plt.plot(x, y, 'g')

plt.grid()
plt.gca().set_ylim([-55, 55])
plt.title('Frequency Spectrum', pad=15, fontweight='bold')
plt.xlabel('Frequency (MHz)', labelpad=10, fontweight='bold')
plt.ylabel('Magnitude (dBm)', labelpad=5, fontweight='bold')
plt.show()
