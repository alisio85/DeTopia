import sys
import subprocess
import ipfshttpclient

# Configurazione IPFS
DECENTRALIZATION = {
    'IPFS_URL': '/ip4/127.0.0.1/tcp/5001'  # Assicurati che questo sia corretto
}

def install_package(package):
    """Funzione per installare un pacchetto usando pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Pacchetto '{package}' installato con successo.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'installazione del pacchetto '{package}': {e}")

# Funzione per controllare la versione di IPFS
def check_ipfs_version(client):
    try:
        ipfs_version = client.version()
        print(f"Connessione a IPFS riuscita! Versione: {ipfs_version['Version']}")
        
        # Controlla se la versione è supportata
        major_version = int(ipfs_version['Version'].split('.')[0])
        if not (4 <= major_version < 8):
            raise Exception(f"Unsupported daemon version '{ipfs_version['Version']}'")
    except Exception as e:
        print(f"Errore durante il controllo della versione IPFS: {e}")
        sys.exit(1)

# Funzione per stabilire la connessione a IPFS
def connect_to_ipfs():
    try:
        client = ipfshttpclient.connect(DECENTRALIZATION['IPFS_URL'])
        check_ipfs_version(client)
        return client
    except Exception as e:
        print(f"Errore durante la connessione a IPFS: {e}")
        return None

# Verifica se ipfshttpclient è installato
try:
    client = connect_to_ipfs()
except ModuleNotFoundError:
    print("ipfshttpclient non è installato. Procedo con l'installazione...")
    install_package("ipfshttpclient")
    client = connect_to_ipfs()

def add_file_to_ipfs(file_path):
    if client is None:
        print("Client IPFS non è disponibile. Assicurati che il demone IPFS sia in esecuzione.")
        return None
    try:
        res = client.add(file_path)
        return res
    except Exception as e:
        print(f"Errore durante l'aggiunta del file a IPFS: {e}")
        return None

def get_file_from_ipfs(file_hash):
    if client is None:
        print("Client IPFS non è disponibile. Assicurati che il demone IPFS sia in esecuzione.")
        return None
    try:
        res = client.cat(file_hash)
        return res
    except Exception as e:
        print(f"Errore durante il recupero del file da IPFS: {e}")
        return None

if __name__ == "__main__":
    # Esempio di utilizzo delle funzioni
    file_to_add = 'path/to/your/file.txt'  # Sostituisci con il tuo file
    print("Aggiunta del file a IPFS...")
    response = add_file_to_ipfs(file_to_add)
    print(f"Risposta dall'IPFS: {response}")


