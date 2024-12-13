#!/usr/bin/env python3


def prime(x):
    """This function is used to verify if
    number is prime or not
    param: x
    return: Boolean
    """
    half = int(x / 2)

    for i in range(1, (x // 2) + 1):
        if x / i == x // i and i != 1:
            return False
    return True


for i in range(0, 30):
    # print(f"NUMBER : [{i}] - {prime(i)} ")
    # print(prime(i))
    if prime(i):
        # print(f"[{i}] - ", end="")
        print(f"[{i}] - ")
