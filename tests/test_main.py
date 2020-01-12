" This file contains the test classes and functions."

# IMPORT MODULES

import unittest, os, sys
sys.path.insert(0,os.path.abspath('../cc_validation'))
from luhn import digits_of, LuhnChecksum, check_issuer


# CLASSES

class TestMain(unittest.TestCase):

    "Main class for testing"

    def setUp(self):

        "Setup function for the class"

        self.issuers = [
                        [340000, "American Express"],
                        [510000, "Mastercard"],
                        [560000, "Maestro"],
                        [400000, "Visa"],
                        [000000, "unknown"]
                       ]

    def test_digits_of(self):

        "Test the function digits_of."

        string = "0123456789012345"
        output = digits_of(string)
        expected_output = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]
        self.assertEqual(output, expected_output)

    def test_LuhnChecksum(self):

        "Test the function LuhnChecksum."

        output = LuhnChecksum("0123456789012345")
        expected_output = 8
        self.assertEqual(output,expected_output)

    def test_check_issuer(self):

        "Test the function check_issuer."

        datafile = os.path.abspath('../data/cc_validation/cc_issuers.csv')
        outputs, expected_outputs = [], []
        for row in self.issuers:
            card_number = str(row[0])
            outputs.append(check_issuer(card_number, datafile))
            expected_outputs.append(row[1])
        self.assertEqual(outputs,expected_outputs)

    def tearDown(self):

        "Teardown function for the class."

        pass
