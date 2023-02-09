# Credits: https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/
# Credits: https://gist.github.com/edy555/08284bcbd03cc59ea9b6c49c8dd733c3

import numpy as np
import scipy.signal as sp
import array
import rtlsdr
import pyaudio
import queue
import signal

def signal_handler(signum, frame):
    exit(-1)
signal.signal(signal.SIGINT, signal_handler)

Fs=2.4e6 # sampling rate
tune=100.7e6 # tuning frequency
gain = 'auto' # LNA gain
length=1024*50

sdr = rtlsdr.RtlSdr(0)
sdr.set_sample_rate(Fs)
sdr.set_manual_gain_enabled(1)
sdr.set_gain(gain)
sdr.set_center_freq(tune)

pa = pyaudio.PyAudio()

que = queue.Queue()

def callback(in_data, frame_count, time_info, status):
    capture = que.get()
    x = np.array(capture).astype('complex64')

    # downsample and filter the signal using remez algorithm
    fm_bw = 240000
    taps = 64
    low_pass_filt = sp.remez(taps, [0, fm_bw, fm_bw+(Fs/2-fm_bw)/4, Fs/2], [1, 0], Hz=Fs)
    x = sp.lfilter(low_pass_filt, 1.0, x)
    dec_rate = int(Fs / fm_bw)
    x = x[0::dec_rate]
    Fs_y = Fs / dec_rate

    # demodulate using polar discriminator
    y = x[1:] * np.conj(x[:-1])
    x = np.angle(y)

    # de-emphasis filter
    d = Fs_y * 10e-4 # EDIT HERE FOR NOISE REDUCTION!!!
    decay_calc = np.exp(-1/d)
    b = [1-decay_calc]
    a = [1, -decay_calc]
    x = sp.lfilter(b,a,x)

    # decimate again to focus mono audio
    audio_freq = 44100.0 # audio sampling rate between 44-48 kHz
    dec_audio = int(Fs_y/audio_freq)
    Fs_audio = Fs_y / dec_audio
    x = sp.decimate(x, dec_audio)
    x = sp.lfilter(low_pass_filt, 1.0, x)
    buf = array.array('f', x).tobytes()
    return (buf, pyaudio.paContinue)

stream = pa.open(format=pyaudio.paFloat32,
                channels=1, rate=int(Fs/50), output=True, stream_callback = callback)
stream.start_stream()

def capture_callback(capture, rtlsdr_obj):
    que.put(capture)

sdr.read_samples_async(capture_callback, length)

stream.stop_stream()
pa.close()
sdr.close()
