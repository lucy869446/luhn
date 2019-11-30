#! /usr/bin/env python3

# IMPORT MODULES

import sys
import argparse
from cc_validation.luhn import isLuhnValid


# DEFINE VARIABLES

#card_number = sys.argv[1]
parser = argparse.ArgumentParser()
parser.add_argument("cn",type=str,help="card number to be validated")
args = parser.parse_args()
card_number = args.cn


# BODY

isLuhnValid(card_number)
