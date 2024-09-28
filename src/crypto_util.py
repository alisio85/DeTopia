# src/crypto_util.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from config import CRYPTO_SETTINGS

class AESCipher:
    def __init__(self):
        self.key = CRYPTO_SETTINGS['ENCRYPTION_KEY']

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
        return cipher.iv + ct_bytes  # Restituisci IV + ciphertext

    def decrypt(self, encrypted_data):
        iv = encrypted_data[:16]  # Prendi i primi 16 byte come IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
        return pt.decode()  # Decodifica i byte in stringa
