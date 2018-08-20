from settings import app
import unittest
import requests
import json
import sys
import subprocess


class TestFlaskApiUsingRequests(unittest.TestCase):
    def setUp(self):
        subprocess.call('docker-compose up & ', shell=True)

    def test_drop_all_data(self):
        response = requests.get('http://localhost:5001/feature/dropall/')
        self.assertEqual(response.json(), {'status': 'Successfully saved a request.'})

    def test_api_create_feature_request(self):
        data={}
        data['title'] = 'Test Title'
        data['description'] = 'Test Description'
        data['client'] = 'Client A'
        data['priority'] = 1
        data['targetDate'] = '2018-8-21'
        data['productArea'] = 'Policies'

        response = requests.post('http://localhost:5001/feature/create/', data=json.dumps(data))
        self.assertEqual(response.json(), {'status': 'Successfully saved a request.'})

    def test_api_get_feature_request(self):
        rv = requests.post('http://localhost:5001/feature/getall/')
        data = rv.json()
        self.assertGreaterEqual(len(data['data']), 1)

if __name__ == '__main__':
    unittest.main()