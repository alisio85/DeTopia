import unittest
from unittest.mock import patch
from src.zeronet_integration import create_site, update_site, get_site_data

class TestZeroNetIntegration(unittest.TestCase):

    @patch('src.zeronet_integration.requests.post')
    def test_create_site(self, mock_post):
        # Configura il mock
        mock_post.return_value.json.return_value = {"success": True, "message": "Site created"}
        
        result = create_site('test_site', 'Test content')
        
        # Asserisci che il risultato sia quello atteso
        self.assertEqual(result['success'], True)
        self.assertEqual(result['message'], "Site created")
        mock_post.assert_called_once_with('http://127.0.0.1:43110/create', json={"site_name": 'test_site', "content": 'Test content'})

    @patch('src.zeronet_integration.requests.post')
    def test_update_site(self, mock_post):
        mock_post.return_value.json.return_value = {"success": True, "message": "Site updated"}
        
        result = update_site('site_address', 'New content')
        
        self.assertEqual(result['success'], True)
        self.assertEqual(result['message'], "Site updated")
        mock_post.assert_called_once_with('http://127.0.0.1:43110/update', json={"site_address": 'site_address', "new_content": 'New content'})

    @patch('src.zeronet_integration.requests.get')
    def test_get_site_data(self, mock_get):
        mock_get.return_value.json.return_value = {"data": "Site data"}
        
        result = get_site_data('site_address')
        
        self.assertEqual(result['data'], "Site data")
        mock_get.assert_called_once_with('http://127.0.0.1:43110/data/site_address')

if __name__ == '__main__':
    unittest.main()
