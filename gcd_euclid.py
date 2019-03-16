# implementation based on https://en.wikipedia.org/wiki/Euclidean_algorithm

def euclid_div(a, b):

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

def euclid_sub(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a # or b


def euclid_rec(a, b):

    # Base case
    if b == 0:
        return a

    # Recursive case
    return euclid_rec(b, a % b)