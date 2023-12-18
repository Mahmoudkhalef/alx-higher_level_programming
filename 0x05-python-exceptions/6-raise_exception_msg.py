#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.strderr)
        is_int = False
    return is_int
