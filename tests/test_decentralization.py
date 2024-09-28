import unittest
from unittest.mock import patch, MagicMock
from src.decentralization import add_file_to_ipfs, get_file_from_ipfs

class TestDecentralization(unittest.TestCase):
    
    @patch('src.decentralization.client')
    def test_add_file_to_ipfs(self, mock_client):
        mock_client.add.return_value = {'Hash': 'Qm1234567890', 'Path': 'file.txt'}
        
        result = add_file_to_ipfs('test_file.txt')
        self.assertIsNotNone(result, "Il risultato non dovrebbe essere None.")
        self.assertEqual(result['Hash'], 'Qm1234567890')

    @patch('src.decentralization.client')
    def test_get_file_from_ipfs(self, mock_client):
        mock_client.cat.return_value = b'This is the content of the file.'
        
        result = get_file_from_ipfs('Qm1234567890')
        self.assertIsNotNone(result, "Il risultato non dovrebbe essere None.")
        self.assertEqual(result, b'This is the content of the file.')

if __name__ == "__main__":
    unittest.main()
