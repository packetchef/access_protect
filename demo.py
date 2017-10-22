#!/usr/bin/env python

import sys
import accessit
import protectit


def main(initialString):
    protectedString = protectit.protect(initialString)
    unprotectedString = accessit.access(protectedString)

    print('Initial string: {0}'.format(initialString))
    print('Protected string: {0}'.format(protectedString))
    print('Unprotected string: {0}'.format(unprotectedString))

    print('Does the unprotected string match the initial string: {0}'.format(initialString == unprotectedString))


if __name__ == '__main__':
    try:
        inputString = sys.argv[1]
    except IndexError:
        inputString = 'This is a standard demo string'

    main(inputString)

