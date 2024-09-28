import unittest
from unittest.mock import AsyncMock, patch
from src.matrix_integration import matrix_login, send_matrix_message

class TestMatrixIntegration(unittest.IsolatedAsyncioTestCase):

    @patch('src.matrix_integration.matrix_client.login', new_callable=AsyncMock)
    async def test_matrix_login_success(self, mock_login):
        mock_login.return_value = AsyncMock()
        await matrix_login()
        mock_login.assert_called_once()

    @patch('src.matrix_integration.matrix_client.room_send', new_callable=AsyncMock)
    async def test_send_matrix_message_success(self, mock_send):
        await send_matrix_message("!testroom:matrix.org", "Ciao DeTopia!")
        mock_send.assert_called_once()

if __name__ == '__main__':
    unittest.main()
