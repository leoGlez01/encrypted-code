import random
import os
import platform

SECRET_KEY_FILE = 'secret_key.txt'

if platform.system() != 'Windows':
    SECRET_KEY_FILE = '.' + SECRET_KEY_FILE

def get_secret_key():
    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'r') as f:
            secret_key = f.read()
    else:
        secret_key = input("Type your secret phrase, please don't share it!")
        with open(SECRET_KEY_FILE, 'w') as f:
            f.write(secret_key)
        
        if platform.system() == 'Windows':
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(SECRET_KEY_FILE, FILE_ATTRIBUTE_HIDDEN)

    return secret_key


def encode(cadena):
    mapping = {
        '''Here your Map Items'''
    }

    nueva_cadena = ""
    for caracter in cadena:
        if caracter in mapping:
            nueva_cadena += mapping[caracter]
        else:
            nueva_cadena += caracter
    
    selfkey = get_secret_key()

    encoded_key = ""
    for char in selfkey:
        if char in mapping:
            encoded_key += mapping[char]
        else:
            encoded_key += char


    secret_key = (
        random.choice("df")
        + random.choice("hj")
        + random.choice("$^")
        + random.choice("%")
        + random.choice("#@")
        + random.choice("!?")
        + random.choice("-_")
        + random.choice("&f")
        + random.choice("vb")
        + "."
        + "L0123"
    )

    encrypted = nueva_cadena + "." + secret_key+"."+ encoded_key
    return encrypted


def decode(cadena):
    map = {
        '''Here your Map Items'''
    }
    map_inv = {v: k for k, v in map.items()}
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in map_inv:
            nueva_cadena += map_inv[caracter]
        elif caracter == ".":
            break
        else:
            nueva_cadena += caracter

    secret = input("Type your secret phrase for decode please!")

    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'r') as f:
            secretfile = f.read()
            if secret != secretfile:
                return ("This phrase is wrong and don't match whit the saved one.")
            else:
                return nueva_cadena
