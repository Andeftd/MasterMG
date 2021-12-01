import logging
import os
import requests
import time
import unittest2


ip_rng = "192.168.49.2:32054"

class Testing(unittest2.TestCase):
    def test_get_random_bytes(self):
        r = requests.get("http://"+ip_rng+"/")
        self.assertEqual("RNG running on rng-594ff5dddf-kmzpx\n", r.text)

if __name__ == '__main__':
    unittest2.main()
