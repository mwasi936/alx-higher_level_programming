#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    
    args = argv[1:]
    args_as_integers = [int(arg) for arg in args]

    result = sum(args_as_integers)

    print(result)
