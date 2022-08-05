#-- Used for sending live video data

# Dependencies
import cv2 # OpenCV Module
import socket, pickle, struct
import imutils
import time, os
import queue
import threading
import base64

# Proof of life
print('vid_trans_caller.py script is running')

# Establish connection (Listen for requests)
BUFF_SIZE = 65336
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 6918
socket_address = (host_ip, port)
server_socket.bind(socket_address)
print('Listening at:', socket_address[0])

# Generate and send video data
vid = cv2.VideoCapture(0)
q = queue.Queue(maxsize=10)

def generate_video():
    Width = 600 # Change video frame size
    while (vid.isOpened()):
        try:
            _, frame = vid.read()
            frame = imutils.resize(frame, width=Width)
            q.put(frame)
        except:
            os._exit(1)
        time.sleep(0.001)
    print('Camera closed')
    BREAK = True
    vid.release()

def transmit_video():
    fps, st, frames_to_count, cnt = (0, 0, 20, 0)
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('Connected to client', client_addr[0])

    while True:
        frame = q.get()
        encoded, buffer = cv2.imencode('.jpeg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)
        server_socket.sendto(message, client_addr)
        frame = cv2.putText(frame, 'FPS: ' + str(round(fps,1)), (1, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        if cnt ==  frames_to_count:
            try:
                fps = round(frames_to_count/(time.time()-st),1)
                st = time.time()
                cnt = 0
            except:
                pass
        cnt+=1

        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1) & 0xFF

        win_state = cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE)
        
        if key == ord('q'):
            os._exit(1)
        elif win_state == 0:
            os._exit(1)
        time.sleep(0.01)

thread_1 = threading.Thread(target = generate_video, args = ())
thread_2 = threading.Thread(target = transmit_video, args = ())
thread_1.start()
thread_2.start()
