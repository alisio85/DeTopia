from flask import Flask
from .user_management import register_user, login_user
from .content_management import create_content

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Gestisci registrazione
    pass

@app.route('/login', methods=['POST'])
def login():
    # Gestisci login
    pass

@app.route('/create_content', methods=['POST'])
def create_content_route():
    # Gestisci creazione contenuto
    pass

if __name__ == "__main__":
    app.run(debug=True)
