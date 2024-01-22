#!/usr/bin/python3
def fizzbuzz(num):
    if num % 3:
        print("Fizz")
    elif num % 5:
        print("Buzz")
    elif num % 3 and num % 5:
        print("FizzBuzz")
    else:
        print(num)
         
