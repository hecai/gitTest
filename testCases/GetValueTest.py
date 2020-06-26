import unittest
import requests


class GetValueCase(unittest.TestCase):

    def test_getValue(self):
        response = requests.get(url="https://www.baidu.com")
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
