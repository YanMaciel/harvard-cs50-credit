# Academic Honesty
If you are taking Harvard's CS50 - Introduction to Computer Science course you **must follow the course's [Academic Honesty philosophy](https://cs50.harvard.edu/x/2021/honesty/)**.

It is not reasonable to access a solution to some assessement prior to (re-)submitting your own.

The essence of all work that you submit to the CS50 course **must be your own**. 

# CS50's Credit
In this exercise we needed to implement a command-line application using Python to validate a credit card number and tell if its flag is MASTERCARD, VISA, AMEX or an INVALID card using Luhn’s Algorithm.

# How it works
This is a command-line application fully developed in **Python**.

The task was to implement Luhn's Algorithm in Python coding and to implement efficient functions to validate the credit card numbers and to organize our code to better optimize the design and its style.

In total I implemented three functions: 

1. To count how many digits the card has;
2. To validate credit card number using Luhn’s algorithm;
3. And one function to get the credit card's number header, used also to validate the credit card.
  
# What I learned
In this exercise, I learned how to define functions and struct a command-line program using Python. It was a great experience because Python is a higher level language than C, so I could compare both of them and learn their differences and similarities.

Got a 100% grade in correctness, design and style in this exercise.

# Usage
To use and test this program, you will need [CS 50 Library](https://cs50.readthedocs.io/libraries/cs50/python/) and [Python](https://www.python.org/downloads/). Copy this repository and through the command-line, enter the program's folder and run the following command:

    $ python credit.py

The application will request a number, where you should input the credit card number to be tested. This is application will not store this number anywhere. [Here](https://developer.paypal.com/docs/payflow/payflow-pro/payflow-pro-testing/) are some fictional credit card numbers Paypal recommend using for tests.

The application will return if the number is a Visa, Mastercard, Amex or invalid credit card:

    $ python3 credit.py
    Number: 4003600000000014
    VISA
    
