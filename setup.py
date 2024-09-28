# setup.py

from setuptools import setup, find_packages

setup(
    name='detopia',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'requests',
        'pycryptodome',  # per la crittografia
        'ipfshttpclient',  # per interagire con IPFS
    ],
    entry_points={
        'console_scripts': [
            'detopia=src.main:main',  # Assicurati di avere una funzione main in main.py
        ],
    },
)
