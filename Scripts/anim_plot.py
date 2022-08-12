# ANIMATED PLOT

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import subprocess as sp

sp.Popen(['python', 'get_data.py'])

x = np.load('x_data.npy', allow_pickle=True)
y = np.load('y_data.npy', allow_pickle=True)

def get_x_y():
    y = np.load('y_data.npy')
    return(y)

fig = plt.figure()
fig.canvas.manager.set_window_title('Frequency Spectrum')
fig.subplots_adjust(bottom=0.15)
line, = plt.plot(x, y, 'g', animated=True)

def init():
    line.set_data(x, y)
    return line,

def animate(i):
    y = get_x_y()
    line.set_data(x, y)
    return line,

plt.grid()
plt.gca().set_ylim([-55, 55])
plt.gca().set_aspect("auto", adjustable='box')
plt.title('Frequency Spectrum', pad=15, fontweight='bold')
plt.xlabel('Frequency (MHz)', labelpad=10, fontweight='bold')
plt.ylabel('Magnitude (dBm)', labelpad=5, fontweight='bold')
ani = FuncAnimation(fig, animate, init_func = init, blit=True, repeat=True)
plt.show()
