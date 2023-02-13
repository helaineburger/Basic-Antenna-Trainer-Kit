from cryptography.fernet import Fernet

def cred():
    cred_file = open('cred', 'a+')
    cred_file.seek(0)
    key = bytes(cred_file.readlines()[0], 'utf-8')
    cred_file.seek(0)
    enc_pword = bytes(cred_file.readlines()[1], 'utf-8')
    cred_file.close()
    
    fernet = Fernet(key)
    pword = str(fernet.decrypt(enc_pword)).strip('b').strip('\'')

    return (pword)
