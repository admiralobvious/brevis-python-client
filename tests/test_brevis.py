import unittest

import brevis
import requests_mock


class TestBrevis(unittest.TestCase):
    def setUp(self):
        base_url = 'mock://brevis'
        self.client = brevis.BrevisClient(base_url)
        self.adapter = requests_mock.Adapter()
        self.client.session.mount('mock', self.adapter)

    def test_shorten(self):
        url = 'http://test.com'
        data = {
            'shortUrl': self.client.base_url + '/Ur4HRbUCN',
            'url': url
        }
        self.adapter.register_uri('POST', self.client.base_url+'/shorten', json=data)
        resp = self.client.shorten(url)

        self.assertDictEqual(data, resp)

    def test_unshorten(self):
        short_url = 'Ur4HRbUCN'
        data = {
            'shortUrl': short_url,
            'url': 'http://test.com'
        }
        self.adapter.register_uri('POST', self.client.base_url+'/unshorten', json=data)
        resp = self.client.unshorten(short_url)

        self.assertDictEqual(data, resp)
