"""
This file contains CC validation functions
"""


def check_issuer(card_number):

    "Function to check CC issuer"

    """
    List containing CC issuers

    Col.1: start of range
    Col.2: end of range
    Col.3: service issuer

    """

    iin_ranges = [
        [340000, 379999, "American Express"],
        [510000, 559999, "Mastercard"],
        [560000, 599999, "Maestro"],
        [400000, 499999, "Visa"]
        ]

    iin = int(card_number[:6])
    for start, end, issuer in iin_ranges:
        if iin >= start and iin <= end:
            return issuer
    return "unknown"


def digits_of(n):

    "Function to create a list of integers from string"

    return [int(d) for d in str(n)]


def LuhnChecksum(card_number):

    "Function to compute the checksum"

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    Checksum = 0
    Checksum += sum(odd_digits)
    for l in even_digits:
        Checksum += sum(digits_of(l*2))
    return Checksum % 10


def isLuhnValid(card_number):

    "Function to print the CC validation"

    """
    Args:
         card_number: string
    """

    if LuhnChecksum(card_number) == 0:
        print((
             "The number that was given as input: {} is a valid CC number")
             .format(card_number))
    else:
        print((
             "The number that was given as input: {} is not a valid CC number")
             .format(card_number))
    print("The issuer is: {}".format(check_issuer(card_number)))
