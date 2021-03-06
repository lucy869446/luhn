"Main file to run."

# IMPORT MODULES

import sys
import argparse
import subprocess
import os
from cc_validation.luhn import isLuhnValid


# PARAMETERS

default_datafile = 'data/cc_validation/cc_issuers.csv'


# FUNCTIONS

def arg_parsing():

    "Function to parse arguments of main.py"

    def str2bool(v):

        "Function to convert a string to a boolean."

        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser()
    parser.add_argument(
                        "mode", type=str,
                        help='type "add" to add a user to db, \
or "validate" to validate a cn.')
    parser.add_argument(
                        "-a",
                        type=str,
                        help="username to be added to db")
    parser.add_argument(
                        "-p",
                        type=str,
                        help="password to be added to db")
    parser.add_argument(
                        "-u",
                        type=str,
                        help="username to access the cn validation")
    parser.add_argument(
                        "-cn",
                        type=str,
                        help="card number to be validated")
    parser.add_argument(
                        "-v",
                        type=str2bool,
                        help="verbosity",
                        default=False)
    args = parser.parse_args()
    mode = args.mode
    username_to_be_added = args.a
    username_for_login = args.u
    password = args.p
    card_number = args.cn
    verbosity = args.v

    return (mode, username_for_login, username_to_be_added,
            password, card_number, verbosity)


def call_dbmanager(username_for_login, username_to_be_added, password):

    "Database managing function."

    abs_path = os.path.dirname(os.path.realpath(__file__))
    abs_path += "/scripts/dbmanager.py"

    if (mode == 'add' and
            username_to_be_added is not None and password is not None):
        exit_code = subprocess.check_output(
                                            ["\
python {} -a {} -p {}".format(abs_path, username_to_be_added, password)],
                                            shell=True)
    elif (mode == 'validate' and
            username_for_login is not None and password is not None):
        exit_code = subprocess.check_output(
                                            ["\
python {} -u {} -p {}".format(abs_path, username_for_login, password)],
                                            shell=True)
    else:
        exit_code = 1

    return exit_code


# BODY

mode, username_for_login, username_to_be_added,
password, card_number, verbosity = arg_parsing()
if mode != "test":
    try:
        exit_code = call_dbmanager(
                                   username_for_login,
                                   username_to_be_added, password)
        if mode == 'validate':
            isLuhnValid(card_number, default_datafile, verbosity)
        elif mode == 'add':
            print('New user added.')
    except Exception:
        print('Error during database operation.')
else:
    isLuhnValid(card_number, default_datafile, verbosity)
