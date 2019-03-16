# implementation based on:
# - Knuth, D. E. (1997). The Art of Computer Programming, Volume 2: Seminumerical Algorithms (3rd ed.). Addison–Wesley.
# - Stillwell, J. (1997). Numbers and Geometry. New York: Springer-Verlag.

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