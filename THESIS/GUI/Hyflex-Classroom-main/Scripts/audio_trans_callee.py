#-- Used for sending live audio data from the caller

# Dependencies
import pyaudio
import socket
import caller_ip
import time

# Proof of life
print('audio_trans_caller.py script is running')

# Establish connection (Send requests)
client_ip = caller_ip.caller_ip # Caller IP
port = 6927
print('Connecting...')
time.sleep(30)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_ip, port))
print('Connected to ', client_ip)
print('Intializing microphone...')

# Generate and send audio
p = pyaudio.PyAudio()
format = pyaudio.paInt16
samp_size = p.get_sample_size(format)
buffer = 1024 * samp_size
#print('Sample size =', samp_size)
input_stream = p.open(format = format, input = True, rate = 44100, channels = 1, frames_per_buffer = buffer)

while True:
    data = input_stream.read(buffer)
    client_socket.sendall(data)
    #print(data)

