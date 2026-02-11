#!/usr/bin/env python3

number = float(input("Give me a number : "))

is_int = number * 10 % 10 == 0

if is_int:
    print("This number is an integer.")
else:
    print("This number is a decimal.")