#导包
import requests
import unittest
import random
#设计用例
class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.url = r'http://localhost:8000/api/departments/'
        self.req_head = {"Content-Type": "application/json"}
    #新增学院
    def test_depPost(self):
        req_data = r'{"data": [{"dep_id":"T17","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)

    #新增学院(消息体断言)
    def test_depPost_1(self):
        req_data = r'{"data": [{"dep_id":"T18","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        # print(a)
        self.assertEqual(a,1)

    def test_depPost_2(self):
        req_data = r'{"data": [{"dep_id":"T19","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_3(self):
        req_data = r'{"data": [{"dep_id":"T20","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_4(self):
        req_data = r'{"data": [{"dep_id":"T21","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_5(self):
        req_data = r'{"data": [{"dep_id":"T22","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_6(self):
        req_data = r'{"data": [{"dep_id":"T23","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_7(self):
        req_data = r'{"data": [{"dep_id":"T24","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_8(self):
        req_data = r'{"data": [{"dep_id":"T25","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_9(self):
        req_data = r'{"data": [{"dep_id":"T26","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_10(self):
        req_data = r'{"data": [{"dep_id":"T27","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_11(self):
        req_data = r'{"data": [{"dep_id":"T28","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_12(self):
        req_data = r'{"data": [{"dep_id":"T29","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

    # 新增学院(消息体断言)
    def test_depPost_13(self):
        req_data = r'{"data": [{"dep_id":"T30","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        resJson = res.json()
        a = resJson.get('create_success').get("count")
        self.assertEqual(a,1)

    def test_depPost_14(self):
        req_data = r'{"data": [{"dep_id":"T31","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url,data=req_data.encode('utf-8'),headers=self.req_head)
        self.assertEqual(201,res.status_code)

if __name__ == '__main__':
    unittest.main()