import unittest
from src.database import reset_database  # Assicurati di importare la funzione per ripristinare il database
from src.user_management import register_user, login_user, get_user_role, update_user_resources

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        reset_database()

    def test_register_user(self):
        result = register_user("testuser", "password123", "user", "testuser@example.com")
        self.assertEqual(result, "User registered successfully.")
        result = register_user("testuser", "password456", "user", "testuser@example.com")
        self.assertEqual(result, "Username already exists.")

    def test_login_user(self):
        register_user("testuser", "password123", "user", "testuser@example.com")
        self.assertEqual(login_user("testuser", "wrongpassword"), "Invalid password.")
        self.assertEqual(login_user("testuser", "password123"), "Login successful.")

    def test_get_user_role(self):
        register_user("testuser", "password123", "admin", "testuser@example.com")
        self.assertEqual(get_user_role("testuser"), "admin")
        self.assertEqual(get_user_role("nonexistentuser"), "User does not exist.")

    def test_update_user_resources(self):
        # Aggiungere test per l'aggiornamento delle risorse degli utenti (da implementare)
        pass

if __name__ == '__main__':
    unittest.main()

