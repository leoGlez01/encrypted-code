
def get_key():
    key = 'xD'

    return key

mapping = {
    '''
    "message":"Your map items here"
    '''
}

def xor_cipher(input_string, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(input_string, key * len(input_string)))

def encode(cadena):
    xor_cadena = xor_cipher(cadena, get_key())

    nueva_cadena = ""
    for caracter in xor_cadena:
        if caracter in mapping:
            nueva_cadena += mapping[caracter]
        else:
            nueva_cadena += caracter

    return nueva_cadena

def decode(cadena):
    map_inv = {v: k for k, v in mapping.items()}
    xor_cadena = ""
    for caracter in cadena:
        if caracter in map_inv:
            xor_cadena += map_inv[caracter]
        else:
            xor_cadena += caracter

    decrypted_cadena = xor_cipher(xor_cadena, get_key())

    return decrypted_cadena
