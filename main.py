#! /usr/bin/env python3
from luhn import isLuhnValid

valid = "4556194895263730"
invalid = "8556194895263730" 

isLuhnValid(valid)
isLuhnValid(invalid)
