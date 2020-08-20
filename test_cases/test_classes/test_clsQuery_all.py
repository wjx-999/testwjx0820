#导包
import requests
import unittest
#设计用例
class TestDepQueryAll(unittest.TestCase):
    def setUp(self) -> None:
        self.url = r'http://127.0.0.1:8000/api/departments/B002/classes/'
        self.res = requests.get(self.url)
    #查询所有
    def test_clsQuery_all(self):
        self.assertEqual(200,self.res.status_code)

    #查询所有(带参)
    def test_clsQuery_all_1(self):
        param = {"cls_id":"2018199"}
        res = requests.get(self.url,param)
        self.assertEqual(200,res.status_code)

    #查询指定
    def test_clsQuery_zd(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/2018196/'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #查询列表
    def test_clsQuery_lb(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?$cls_id_list=2018196,2018885'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #查询列表(cls_name)
    def test_clsQuery_lb_1(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?$cls_name_list=2018级Test学院C015班,2018级Test学院C016班'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    # 查询列表(cls_master)
    def test_clsQuery_lb_2(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?$cls_master_list=Master16,Master15'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    # 查询列表(cls_slogan)
    def test_clsQuery_lb_3(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?$cls_slogan_list=slogan16,slogan15'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #列表组合查询
    def test_clsQuery_lbzh(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?$cls_id_list=2018965,2018885&$master_name_list=Master16,Master15'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #条件查询
    def test_clsQquery_tj(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?cls_name=2018级Test学院C016班'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #条件组合查询
    def test_clsQuery_tjzh(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?cls_name=2018级Test学院C016班&master_name=Master16&slogan=slogan16'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #模糊查询
    def test_clsQuery_mh(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?blur=1&cls_name=2018级'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #blur设置为0
    def test_clsQuery_mh_1(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?blur=0&cls_name=2018级'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #模糊组合查询
    def test_clsQuery_mhzh(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?blur=1&cls_name=2018级&master_name=16'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

    #blur设置为0
    def test_clsQuery_mhzh_1(self):
        url = r'http://127.0.0.1:8000/api/departments/B002/classes/?blur=0&cls_name=2018级&master_name=16'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)

if __name__ == '__main__':
    unittest.main()