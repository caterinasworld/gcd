# implementation based on https://en.wikipedia.org/wiki/Binary_GCD_algorithm
# using variables a and b instead of u and v for consistency

def binary_gcd_loops(a, b):

    shift = 0

    # simple cases (termination)
    if (a == 0):
        return b

    if (b == 0):
        return a

    # Find greatest power of 2 dividing both u and v
    while (((a | b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        shift = shift + 1

    # Dividing a by 2 until a becomes odd
    while ((a & 1) == 0):
        a = a >> 1

    # From here on, 'a' is always odd
    while (b != 0):

        # remove all factors of 2 in b
        while ((b & 1) == 0):
            b = b >> 1

        # Now a and b are both odd. Swap if necessary so a <= -b
        if (a > b):
            temp = a
            a = b
            b = temp

        b = b - a

        # restore common factors of 2
    return a << shift


def binary_gcd_rec(a, b):

    # simple cases (termination)
    if (a == b):
        return a

    if (a == 0):
        return b

    if (b == 0):
        return a

    # look for factors of 2
    if (~a & 1): # a is odd

        # b is odd
        if (b & 1):
            return binary_gcd_rec(a >> 1, b)
        else:
            # both a and b are even
            return (binary_gcd_rec(a >> 1, b >> 1) << 1)

    # a is odd, b is even
    if (~b & 1):
        return binary_gcd_rec(a, b >> 1)

    # reduce larger number
    if (a > b):
        return binary_gcd_rec((a - b) >> 1, b)

    return binary_gcd_rec((b - a) >> 1, a)