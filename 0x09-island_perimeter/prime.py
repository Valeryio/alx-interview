#!/usr/bin/env python3


def prime(x):
    """This function is used to verify if
    number is prime or not
    param: x
    return: Boolean
    """
    for i in range(1, (x // 2) + 1):
        if x / i == x // i and i != 1:
            return False
    return True

def primelist(mylist):
    newlist = []

    for i in mylist:
        if prime(i):
            newlist.append(i)
    return newlist

def remove_mul(x, mylist):
    """This function is uused to remove the
    multiple of a number from a list
    param: x (multiple to use)
    param: mylist (original list to check)
    return: newlist
    """
    newlist = []
    for i in mylist:
        print(f"This is I : [{i}]")
        print(f"{i} / {x} = {i / x} \t\t {x} / {i} = {x / i}")
        if i / x != i // x:
            newlist.append(i)

    return newlist

def isWinner(x, mylist):
    """
    This function is used to find the user
    of the game played
    param: x (number of rounds)
    param: mylist (list of n of each round)
    """

    players = {"Marie": 0, "Ben": 0}

    for n in range(x):
        tours = 0
        myset = [m for m in range(mylist[n])]
        print(f"This is my set : {myset}")
        myset_primes = primelist(myset)
        print(f"THis is my set primes : {myset_primes}")

        for i in range(myset_primes):
            if i / 2 == i // 2:
                print("C'est au tour de Ben")
            else:
                print("C'est au tour de Marie")
            tours += 1
            myset = remove_mul(i, myset)
        
        if tours / 2 == tours // 2:
            players["Ben"] += 1
        else:
            players["Marie"] += 1

    if players["Ben"] > players["Marie"]:
        print("Ben a gagne la partie !!!")
    else:
        print("Marie a gagne la partie")
