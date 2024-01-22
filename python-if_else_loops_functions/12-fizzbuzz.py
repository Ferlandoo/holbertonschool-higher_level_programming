#!/usr/bin/python3
def fizzbuzz(num):
    if num % 3:
        print("Fizz", end=" ")
    elif num % 5:
        print("Buzz", end=" ")
    elif num % 3 and num % 5:
        print("FizzBuzz", end=" ")
    else:
        print(num, end=" ")
         
