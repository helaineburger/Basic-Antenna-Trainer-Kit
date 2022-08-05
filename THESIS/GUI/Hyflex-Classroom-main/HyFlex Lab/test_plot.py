# test

#from pylab import *
import matplotlib.pyplot as plt
from rtlsdr import *
import time

sdr = RtlSdr()

def get_cent_freq_power(samp_rate, cent_freq, gain):

    # configure device
    sdr.sample_rate = samp_rate # 2.4e6
    sdr.center_freq = cent_freq # 95e6
    sdr.gain = gain # 4

    samples = sdr.read_samples(256*1024)

    try:
        plt.close()
    except:
        pass
    
    fig, (ax) = plt.subplots(1,1)

    # use matplotlib to estimate and plot the PSD
    ax.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, data=samples)
    line = ax.lines[0]
    db = line.get_ydata()
    print(samples)
    print(db[512])
    time.sleep(3)


def freq_spectrum_plot(samp_rate, cent_freq, gain):
    
    # configure device
    sdr.sample_rate = samp_rate # 2.4e6
    sdr.center_freq = cent_freq # 95e6
    sdr.gain = gain # 4

    samples = sdr.read_samples(256*1024)

    try:
        plt.close()
    except:
        pass
    
    fig, (ax) = plt.subplots(1,1)
    fig.canvas.manager.set_window_title('Frequency Spectrum')

    # use matplotlib to estimate and plot the PSD
    ax.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, data=samples)
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Relative power (dB)')
    line = ax.lines[0]
    db = line.get_ydata()
    print(db[512])
    plt.draw()
    plt.pause(5)
    

#while True:
#get_cent_freq_power(2.4e6, 95e6, 4)
freq_spectrum_plot(2.4e6, 440e6, 4)
    
