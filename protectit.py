#!/usr/bin/env python

import sys

from base64 import b64encode
from binascii import hexlify

def protect(unprotectedString):
	mystring_hex_and_64 = hexlify(b64encode(unprotectedString))
	newstring = ''
	for char in mystring_hex_and_64:
	    newchar = int(hexlify(char)) + 1
	    newstring += str(newchar)

	return newstring


def main(args):
	print(protect(args))


if __name__ == '__main__':
	main(sys.argv[1])


