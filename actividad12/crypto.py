from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def generar_clave_y_iv():
    # Genera una clave de 32 bytes y un IV de 16 bytes, ambos aleatorios
    key = urandom(32)
    iv = urandom(16)
    return key, iv

def encriptar(texto_plano, key, iv):
    # Crea el cifrador AES en modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Convierte el texto a bytes
    texto_plano_bytes = texto_plano.encode('utf-8')
    # Calcula y añade padding para que la longitud sea múltiplo de 16
    padding_length = 16 - (len(texto_plano_bytes) % 16)
    padding = bytes([padding_length]) * padding_length
    texto_a_cifrar = texto_plano_bytes + padding
    # Encripta el texto con padding
    texto_cifrado = encryptor.update(texto_a_cifrar) + encryptor.finalize()
    return texto_cifrado

def desencriptar(texto_cifrado, key , iv):
    # Crea el descifrador AES en modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Descifra el texto
    texto_desencriptado_con_padding = decryptor.update(texto_cifrado) + decryptor.finalize()
    # Elimina el padding
    padding_length = texto_desencriptado_con_padding[-1]
    texto_desencriptado = texto_desencriptado_con_padding[:-padding_length]
    # Devuelve el texto original
    return texto_desencriptado.decode('utf-8')

# Genera clave y IV
key, iv = generar_clave_y_iv()
# Texto a cifrar
texto_original = "Gerardo Martinez Puente."
# Cifra el texto
texto_encriptado = encriptar(texto_original, key, iv)
print(f"Texto encriptado: {texto_encriptado}")
# Descifra el texto
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print(f"Texto desencriptado: {texto_desencriptado}")
