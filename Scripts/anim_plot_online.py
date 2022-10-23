# ANIMATED PLOT

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import subprocess as sp
import pickle
import mysql.connector
import time

#sp.Popen(['python', 'send_data_online.py'])
print('Intializing')
time.sleep(2)

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = 'AVNS_KtBYvuN3xrywbxjVmBz'
db_database = 'signaldata'

db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
db_cursor = db.cursor()

query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1"
db_cursor.execute(query)
result = db_cursor.fetchone();

x = pickle.loads(result[0])
y = pickle.loads(result[1])

db.commit()

def get_x_y():
    db_cursor.execute(query)
    result = db_cursor.fetchone();
    y = pickle.loads(result[1])
    db.commit()
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
