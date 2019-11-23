#! /usr/bin/env python3

# IMPORT MODULES

import sys
from cc_validation.luhn import isLuhnValid


# DEFINE VARIABLES

card_number = sys.argv[1]


# BODY

isLuhnValid(card_number)
