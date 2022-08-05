#-- Used for recieving live video data

# Dependencies
import cv2 # OpenCV Module
import numpy as np
import socket, pickle, struct
import imutils
import time, os
import threading
import base64
import callee_ip

# Proof of life
print('vid_rec_caller.py script is running')

# Establish connection (Send requests)
BUFF_SIZE = 65536
BREAK = False
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
server_ip = callee_ip.callee_ip
port = 6917 

# Recieve and process video data
def recieve_video():
    fps, st, frames_to_count, cnt = (0, 0, 20, 0)
    message = b'Hello'
    print('Connecting...')
    time.sleep(30)
    client_socket.sendto(message, (server_ip, port))
    print('Connected to', server_ip)
    print('Initializing camera...')
    client_socket.settimeout(5)
    
    while True:
        try:
            packet, _ = client_socket.recvfrom(BUFF_SIZE)
            data = base64.b64decode(packet, ' /')
            npdata = np.fromstring(data, dtype = np.uint8)
            
            frame = cv2.imdecode(npdata, 1)
            frame = cv2.putText(frame, 'FPS: ' + str(fps), (1, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            cv2.imshow('Feed', frame)
            key = cv2.waitKey(1) & 0xFF
            
            win_state = cv2.getWindowProperty('Feed', cv2.WND_PROP_VISIBLE)
            
            if key == ord('q'):
                os._exit(1)
            elif win_state == 0:
                os._exit(1)
                
            if cnt == frames_to_count:
                try:
                    fps = round(frames_to_count/(time.time()-st), 1)
                    st = time.time()
                    cnt=0
                except:
                    pass
            cnt+=1
            time.sleep(0.001)
        except socket.error:
            os._exit(1)
        
    client_socket.close()
    cv2.destroyAllWindows()

thread_1 = threading.Thread(target=recieve_video, args=())
thread_1.start()
