# GET RTL-SDR DATA

import matplotlib.pyplot as plt
import numpy as np
from rtlsdr import *
import time

sdr = RtlSdr()

samp_rate = 2.4e6
cent_freq = 440e6
gain = 4

def get_data(sample_rate, cent_freq, gain):
    
    sdr.sample_rate = samp_rate
    sdr.center_freq = cent_freq
    sdr.gain = gain

    samples = sdr.read_samples(256*1024)

    fig, (ax) = plt.subplots(1,1)
    ax.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, data=samples)
    line = ax.lines[0]
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    np.save('x_data', x_data, allow_pickle=True, fix_imports=True)
    np.save('y_data', y_data, allow_pickle=True, fix_imports=True)
    plt.close() # Do not remove to prevent memory leak!!!


try:
    while True:
        get_data(samp_rate, cent_freq, gain)
except:
    print('Invalid frequency configuration.')
