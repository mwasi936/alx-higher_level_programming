#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10
    return last_digit


print(print_last_digit(98), end='')
print(print_last_digit(0), end='')
print(print_last_digit(-1024), end='')
