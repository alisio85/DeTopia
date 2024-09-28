# config.py

import os

# Funzione per generare una chiave segreta sicura
def generate_secret_key():
    return os.urandom(24)  # Genera una chiave segreta di 24 byte

# Database configuration
DATABASE = {
    'NAME': 'detopia.db',
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': ''
}

DECENTRALIZATION = {
    'IPFS_URL': '/ip4/127.0.0.1/tcp/5001',
    'ZERONET_URL': 'http://localhost:43110',
    'MATRIX_URL': 'https://matrix.org',
    'MATRIX_USER': 'detopia_user',
    'MATRIX_PASSWORD': 'yourpassword'
}


# Cryptography settings
CRYPTO_SETTINGS = {
    'ENCRYPTION_KEY': generate_secret_key(),  # Chiave segreta generata
}

# Other settings
OTHER_SETTINGS = {
    'LANGUAGE': 'en',
}
