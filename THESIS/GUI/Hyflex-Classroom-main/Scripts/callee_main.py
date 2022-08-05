import socket
import subprocess as sp

print('callee_main script running...')

def call_listener():
    hostname = socket.gethostname()
    port = 6938
    listen_socket = socket.socket()
    listen_socket.bind((hostname, port))
    listen_socket.listen(5)
    con, addr = listen_socket.accept()

    get_caller_ip = addr[0]
    
    write_caller_ip = open('caller_ip.py', 'w')
    write_caller_ip.write('caller_ip = \'%s\'' % get_caller_ip);
    write_caller_ip.close()

    sp_ar = sp.Popen(['python', 'audio_rec_callee.py'])
    sp_at = sp.Popen(['python', 'audio_trans_callee.py'])
    sp_vr = sp.Popen(['python', 'vid_rec_callee.py'])
    sp_vt = sp.Popen(['python', 'vid_trans_callee.py'])
    
    while True:
        check_proc_live_1 = (sp_vr.poll())
        check_proc_live_2 = (sp_vt.poll())

        if (check_proc_live_1 == None) and (check_proc_live_2 == None):
            pass
        elif check_proc_live_1 == 1:
            sp_ar.kill()
            sp_at.kill()
            sp_vt.kill()
        elif check_proc_live_2 == 1:
            sp_ar.kill()
            sp_at.kill()
            sp_vr.kill()
        else:
            sp_ar.kill()
            sp_at.kill()
            sp_vr.kill()
            sp_vt.kill()

while True:            
    call_listener()
