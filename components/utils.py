import os, json, re
import hashlib

import tkinter as tk

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

from components.schemas import *

salt_len = 16

def hash_password(password):
    salt = os.urandom(salt_len)
    hashed_password = hashlib.sha256(password.encode()).digest() + salt
    return hashed_password.hex()

def get_digest(password_hex):
    password_digest = bytes.fromhex(password_hex)
    return password_digest[:len(password_digest) - salt_len]

def validate_password(input, from_dir):
    hashed_password = hashlib.sha256(input.encode()).digest()
    from_dir = get_digest(from_dir)
    if hashed_password == from_dir:
        return True
    return False


def generate_keypair(password_hex):
    #Phát sinh cặp khóa (Kpublic, Kprivate) qua RSA
    keyPair = RSA.generate(2048)
    Kpublic = keyPair.publickey().export_key()
    #Băm passphase
    Ksecret = get_digest(password_hex)
    Kprivate = keyPair.export_key()
    
    #Mã hóa Kprivate qua AES
    obj = AES.new(Ksecret, AES.MODE_CBC)
    encrypted_text = obj.iv + obj.encrypt(pad(Kprivate, AES.block_size))
    return Kpublic, Kprivate, encrypted_text

def decrypt_Kprivate(encrypted_text, password_hex):
    #Giải mã Kprivate
    Ksecret = get_digest(password_hex)
    iv = encrypted_text[:AES.block_size]
    rev_obj = AES.new(Ksecret, AES.MODE_CBC, iv)
    decrypted_text = rev_obj.decrypt(encrypted_text[AES.block_size:])
    return unpad(decrypted_text,AES.block_size)

def forget_old_widgets(frame: tk.Frame):
    if frame.children:
        while frame.children.values():
            widget = list(frame.children.values())[0]
            widget.destroy()
            
    
def get_user(user_key):
    users = dict()
    with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
        users  = json.load(input)
    for i in users['data']:
        if i['key'] == user_key:
            user = User(i)
            return user
    return None

def get_storage_dir(user_key):
    users = dict()
    with open('data/users_log_data.json', 'r', encoding='utf-8') as input:
        users  = json.load(input)
    for i in users['data']:
        if i['key'] == user_key:
            user = User(i)
            storage = user.storage
            return storage
    return None
def get_password(user_key):
    user = get_user(user_key)
    if user:
        return  user.password
    else: return None

def get_kpublic(user_key):
    user = get_user(user_key)
    if not user:
        return b''
    path = 'data/' + user.storage + '/Kpublic.pub'
    with open(path, 'rb') as publicFile:
        key = publicFile.read()
    publicFile.close()
    return key

def get_enKprivate(user_key):
    user = get_user(user_key)
    if not user:
        return b''
    path = 'data/' + user.storage + '/Kprivate.enc'
    with open(path, 'rb') as private_file:
        enc_key = private_file.read()
    return enc_key

def encrypt_file(file_in, user_to_send_key):              #4.2  +  4.3
    fileIn = open(file_in, 'rb')
    storage_dir = get_storage_dir(user_to_send_key)
    file_name = file_in.split('/')[-1]
    if not storage_dir:
        return False
    file_out = 'data/' + storage_dir
    name = file_name
    if '.' in file_name:
        name = file_name.split('.')[0]
    file_name = file_name.replace(name, name + '_encrypted')
    file_out += '/' + file_name
    fileOut = open(file_out, 'wb+')
    bs = AES.block_size #16 bytes
    Ksession = os.urandom(bs)

    cipher = AES.new(Ksession, AES.MODE_CBC)
    finished = False
    fileOut.write(cipher.iv)
    
    key = RSA.importKey(get_kpublic(user_to_send_key))
    publickey = PKCS1_OAEP.new(key)
    
    encrypted = publickey.encrypt(Ksession)                 #4.3

    fileOut.write(encrypted)

    while not finished:
        chunk = fileIn.read(1024 * bs) 
        if len(chunk) == 0 or len(chunk) % bs != 0:   
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += str.encode(padding_length * chr(padding_length))
            finished = True
        fileOut.write(cipher.encrypt(chunk))                    #4.2
    
    fileIn.close()
    fileOut.close()
    return True
    
def decryptKsession(Kprivate, encrypted_Ksession):              #5.3
    key = RSA.importKey(Kprivate)
    privatekey = PKCS1_OAEP.new(key)
    decrypted = privatekey.decrypt(encrypted_Ksession)
    return decrypted

def decrypt_file(file_in, user_private_key):                     #5.4
    fileIn = open(file_in, 'rb')
    matches = re.findall(r'/\w+',file_in)
    file_name = matches[-1]
    file_name = file_name[1:]
    if file_name.find('_encrypted') != -1:
        file_name.replace('_encrypted','')
    file_out = file_in.replace(file_name, file_name + '_decrypted')
    fileOut = open(file_out, 'wb+')
    bs = AES.block_size #16 bytes
    iv = fileIn.read(bs)

    encrypted_Kprivate = get_enKprivate(user_private_key)
    password_encode = get_password(user_private_key)
    if not password_encode:
        return False
    password_encode.encode()
    cont = fileIn.read(289-33)

    deKprivate = decrypt_Kprivate(encrypted_Kprivate, password_encode)

    Ksession = decryptKsession(deKprivate, cont) 
    
    cipher = AES.new(Ksession, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(fileIn.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = chunk[-1]
            chunk = chunk[: - padding_length]  # type: ignore
            finished = True 
        fileOut.write(bytes(x for x in chunk))   # type: ignore
    return True
