import socket
import subprocess as sp
import contacts
import os

print('caller_main script running...')

def call(contact_name):
    callee_ip = contacts.contacts[contact_name]
    write_callee_ip = open('callee_ip.py', 'w')
    write_callee_ip.write('callee_ip = \'%s\'' % callee_ip);
    write_callee_ip.close()
    port = 6938
    connect_call = socket.socket()
    connect_call.connect((callee_ip, port))
    print('Handshake successful')
    
    sp_at = sp.Popen(['python', 'audio_trans_caller.py'])
    sp_ar = sp.Popen(['python', 'audio_rec_caller.py'])
    sp_vt = sp.Popen(['python', 'vid_trans_caller.py'])
    sp_vr = sp.Popen(['python', 'vid_rec_caller.py'])

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
