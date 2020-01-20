# -*- coding: utf-8 -*-
"""
Greeting script for rotation purposes
"""

import sys
import argparse

parser = argparse.ArgumentParser(description='Greetings script manual.')
parser.add_argument("-u", action = "store", type = str, help = "Changes entry string to uppercase")
parser.add_argument("-l", action = "store", type = str, help = "Changes entry sting to lowercase")
parser.add_argument("-i", action = "store", type = str, help = "Doesn't do shit to entry string (case insensitive)")
args = parser.parse_args()
if args.u:
    print("Executing {} script\n\n".format(sys.argv[0].upper()))
    print("Hello {}\n".format(sys.argv[-1].upper()))
elif args.l:
    print("Executing {} script\n\n".format(sys.argv[0].lower()))
    print("Hello {}\n".format(sys.argv[-1].lower()))
else:
    print("Executing {} script\n\n".format(sys.argv[0]))
    print("Hello {}\n".format(sys.argv[-1]))

