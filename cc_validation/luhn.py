"""
This file contains CC validation functions
"""

import csv


def check_issuer(card_number, datafile):

    "Function to check CC issuer"

    """
    Args:
        - card_number: string
        - data_file: string
    """

    def parse_cc_issuers(datafile):
        iin_ranges = []
        with open(datafile, "r") as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                iin_ranges.append(row)
        for i in range(len(iin_ranges)):
            for j in range(2):
                iin_ranges[i][j] = int(iin_ranges[i][j])
        return iin_ranges

    iin_ranges = parse_cc_issuers(datafile)

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


def isLuhnValid(card_number, datafile, verbosity):

    "Function to print the CC validation"

    """
    Args:
         card_number: string
         verbosity: boolean
    """

    if verbosity:
        service_string = "The issuer is: "

        if LuhnChecksum(card_number) == 0:
            print((
                 "The number that was given as input: {} is a valid CC number")
                 .format(card_number))
        else:
            print((
                 "The number that was given as input: {} \
is not a valid CC number")
                 .format(card_number))
    else:
        service_string = ""

    print("{}{}".format(service_string, check_issuer(card_number, datafile)))
