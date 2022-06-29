#!/usr/bin/python3
for alph in range(26):
    if alph != 4 and alph != 16:
        print("{:s}".format(chr(alph + ord("a"))), end="")
