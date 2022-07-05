#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for a in item:
            print("{:d}".format(a), end="")
            if a != item[-1]:
                print(" ", end="")
        print("")
