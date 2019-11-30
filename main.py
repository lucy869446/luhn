#! /usr/bin/env python3

# IMPORT MODULES

import sys
import argparse
from cc_validation.luhn import isLuhnValid


# FUNCTIONS

def arg_parsing():
    "Function to parse arguments of main.py"

    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser()
    parser.add_argument("cn", type=str, help="card number to be validated")
    parser.add_argument("-v", type=str2bool, help="verbosity", default=False)
    args = parser.parse_args()
    card_number = args.cn
    verbosity = args.v
    return card_number, verbosity


# BODY

card_number, verbosity = arg_parsing()
isLuhnValid(card_number, verbosity)
