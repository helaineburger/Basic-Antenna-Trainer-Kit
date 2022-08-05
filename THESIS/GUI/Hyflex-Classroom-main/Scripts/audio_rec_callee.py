#-- Used for recieving live audio data

# Dependencies
import pyaudio
import socket
import os

# Proof of life
print('audio_rec_callee.py is running')

# Establish connection (Listen for requests)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = socket.gethostbyname(socket.gethostname())
port = 6928
server_address = host_ip, port
server_socket.bind(server_address)
server_socket.listen(5)
print('Connecting...')
conn, addr = server_socket.accept()
print('Connected to', addr[0])

# Recieve and process audio
p = pyaudio.PyAudio()
format = pyaudio.paInt16
samp_size = p.get_sample_size(format)
buffer = 1024 * samp_size
#print('Sample size =', samp_size)

output_stream = p.open(format = format, output = True, rate = 44100, channels = 1, frames_per_buffer = buffer)
data = conn.recv(buffer)
cnt = 0
i = 1

while data != '':
    output_stream.write(data)
    try:
        data = conn.recv(buffer)
    except:
        os._exit(1)
    i = i + 1
    #print(i)
