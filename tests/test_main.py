import unittest
import os
import shutil


class TestMain(unittest.TestCase):

    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(self.path+'/tmp'):
            shutil.rmtree(self.path+"/tmp")
        os.mkdir(self.path+'/tmp/')
        self.issuers = [
                        [340000, 379999, "American Express"],
                        [510000, 559999, "Mastercard"],
                        [560000, 599999, "Maestro"],
                        [400000, 499999, "Visa"]
                       ]

    def test_valid_entries(self):
        for issuer_data in self.issuers:
            issuer = issuer_data[2]
            start = issuer_data[0]
            stop = issuer_data[1]+1
            for cn in range(start, stop, 1000):
                tmp_file = "{}/tmp/tmp.txt".format(self.path)
                os.system("python main.py test -cn {} > {}".format(cn,
                          tmp_file))
                with open(tmp_file) as f:
                    read_issuer = f.read().replace('\n', '')
                    self.assertEqual(read_issuer, issuer)

    def test_invalid_entries(self):
        for start, stop in [[380000, 400000], [500000, 510000]]:
            for cn in range(start, stop, 1000):
                tmp_file = "{}/tmp/tmp.txt".format(self.path)
                os.system("python main.py test -cn {} > {}".format(cn,
                          tmp_file))
                with open(tmp_file) as f:
                    read_issuer = f.read().replace('\n', '')
                    self.assertEqual(read_issuer, 'unknown')

    def tearDown(self):
        shutil.rmtree(self.path+"/tmp")
