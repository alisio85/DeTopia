from nio import AsyncClient, LoginResponse

from config import DECENTRALIZATION

# Configurazione del client Matrix
matrix_client = AsyncClient(DECENTRALIZATION['MATRIX_URL'], DECENTRALIZATION['MATRIX_USER'])

# Funzione per effettuare il login al server Matrix
async def matrix_login():
    try:
        response = await matrix_client.login(DECENTRALIZATION['MATRIX_PASSWORD'])
        if isinstance(response, LoginResponse):
            print("Login a Matrix avvenuto con successo.")
        else:
            print(f"Errore nel login: {response}")
    except Exception as e:
        print(f"Errore nella connessione a Matrix: {e}")

# Funzione per inviare un messaggio in una stanza Matrix
async def send_matrix_message(room_id, message):
    try:
        await matrix_client.room_send(
            room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": message}
        )
        print("Messaggio inviato con successo.")
    except Exception as e:
        print(f"Errore nell'invio del messaggio: {e}")
