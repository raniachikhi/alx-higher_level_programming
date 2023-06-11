#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mati in matrix:
        l = 1
        for matj in mati:
            if l == len(mati):
                print("{:d}".format(matj), end="")
            else:
                print("{:d}".format(matj), end=" ")
            l = l + 1
        print()
