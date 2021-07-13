# Determines whether a provided credit card number is valid according to Luhn’s algorithm
from cs50 import get_int
import sys


def main():

    number = get_int("Numbers: ")
    # Counts how many digits the card has.
    digits = card_digits(number)

    # Apply Luhn’s algorithm and already exits the program if it's not a valid number.
    luhn = validate_card(number)
    if luhn == False:
        print("INVALID")
        sys.exist()

    # Checks the first two digits (header) of the card.
    header = card_header(number)

    # Checks if it's AMEX, VISA or MASTERCARD
    if digits == 15 and (header == 34 or header == 37):
        print("AMEX")
    elif digits == 16 and header > 50 and header < 56:
        print("MASTERCARD")
    elif header > 39 and header < 50 and (digits == 13 or digits == 16):
        print("VISA")
    else:
        print("INVALID")

# Counts how many digits the card has.


def card_digits(n):
    digits = 0
    while n > 0:
        n = int(n / 10)
        digits += 1
    return digits

# Validates credit card number using Luhn’s algorithm


def validate_card(n):
    sum_all = 0  # A kind of counter to later validate the credit card number.
    digits = 0
    while n > 0:
        n = int(n / 10)
        digits += 1
    for i in (1, digits + 1):  # Iterates over credit card number.
        if i % 2 == 0:
            d_mult = (n % 10) * 2  # Goes from last digit to the begining.
            # Converts 2 digits numbers into the sum of its single digits by subtracting 9.
            if d_mult > 9:
                d_mult -= 9
            sum_all += d_mult  # Adds to the sum_all variable.

        if i % 2 != 0:
            d_sum = n % 10
            sum_all += d_sum  # Adds to the sum_all variable.

        n = n / 10  # Goes from last digit to the begining.

    if sum_all % 10 == 0:
        return True
    if sum_all % 10 != 0:
        return False

# Return credit card's number header.


def card_header(n):
    while n > 99:
        n = n / 10
    return int(n)


if __name__ == "__main__":
    main()