#! /usr/bin/env python3

# IMPORT MODULES

from cc_validation.luhn import isLuhnValid


# DEFINE VARIABLES

valid = "4556194895263730"
invalid = "8556194895263730" 


# BODY

isLuhnValid(valid)
isLuhnValid(invalid)
