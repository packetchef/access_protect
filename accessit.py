#!/usr/bin/env python

import sys

from base64 import b64decode
from binascii import unhexlify


def access(protectedString):
	number_of_bytes = len(protectedString) / 2
	currentchar = 0
	endchar = 0
	my64str = ''
	while endchar < len(protectedString):
	    endchar = currentchar + 2
	    mybyte = protectedString[currentchar:endchar]
	    mynewbyte = int(mybyte) - 1
	    my64str += unhexlify(str(mynewbyte))
	    currentchar += 2

	return b64decode(unhexlify(my64str))


def main(args):
	print(access(args))


if __name__ == '__main__':
	main(sys.argv[1])




