#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

first = add(a, b)
second = sub(a, b)
third = mul(a, b)
fourth = div(a, b)

print("{} + {} = {}".format(a, b, first))
print("{} - {} = {}".format(a, b, second))
print("{} * {} = {}".format(a, b, third))
print("{} / {} = {}".format(a, b, fourth))
