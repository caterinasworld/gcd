# implementation based on "A Comparison of Several Greatest Common Divisor Algorithms"
# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.259.1877&rep=rep1&type=pdf

def brute_force(a, b):

    gcd = 0

    # check whether a or b is the lower value
    if a > b:
        low = b
    else:
        low = a

    for i in range(1, low + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd