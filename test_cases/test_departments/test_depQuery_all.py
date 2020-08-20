#导包
import requests
import unittest
#设计用例
class TestDepQueryAll(unittest.TestCase):
    def setUp(self) -> None:
        self.url = r'http://localhost:8000/api/departments/'
        self.res = requests.get(self.url)
    def test_depQuery_all(self):
        self.assertEqual(200,self.res.status_code)
    def test_depQuery_zd(self):
        res = requests.post(self.url)
        self.assertEqual(200,res.status_code)

if __name__ == '__main__':
    unittest.main()