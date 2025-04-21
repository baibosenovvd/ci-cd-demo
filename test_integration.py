import unittest
from unittest.mock import patch
from file1 import main_process

class TestIntegration(unittest.TestCase):

    @patch('file2.second_function')
    def test_valid_data(self, mock_second):
        mock_second.return_value = "✅ Успешно обработано: 20"
        result = main_process(10)
        self.assertEqual(result, "✅ Успешно обработано: 20")
        mock_second.assert_called_once_with(20)

    @patch('file2.second_function')
    def test_zero_data(self, mock_second):
        result = main_process(0)
        self.assertEqual(result, "✅ Успешно обработано: 0")
        mock_second.assert_called_once_with(0)

    @patch('file2.second_function')
    def test_negative_data(self, mock_second):
        result = main_process(-5)
        self.assertIsNone(result)
        mock_second.assert_not_called()

    @patch('file2.second_function')
    def test_empty_data(self, mock_second):
        result = main_process(None)
        self.assertIsNone(result)
        mock_second.assert_not_called()

    def test_log_error(self):
        from file1 import log_error
        with self.assertLogs('root', level='ERROR') as log:
            log_error("Тестовая ошибка")
        self.assertIn("Тестовая ошибка", log.output[0])

if __name__ == "__main__":
    unittest.main()
