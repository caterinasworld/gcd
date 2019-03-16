# import modules
import random
from time import process_time
import csv
import sys
from gcd_euclid import euclid_div, euclid_sub, euclid_rec
from gcd_binary import binary_gcd_loops, binary_gcd_rec
from gcd_naive import brute_force

# find out current recursion limit and reset the limit
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)

# generate random number based on various input bit sizes
# input: any positive integer x
# output: 2^x
def generate_num(x):
    return random.getrandbits(2**x)

# write results to a data file "output" in the "data" folder
def write_to_cvs(outfile, headers, results):
    with open(outfile, mode="wt", encoding="utf-8", newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)

        for i in range(len(results)):
            writer.writerow(results[i])

# time algorithm using time.process_time()
def time_algo(algo, i, a, b, str):

    # time algorithm and keep track of gcd
    # because we run all algorithms in run_all() with the same a and b values
    # the gcd returned for each iteration should be the same
    t1 = process_time()
    gcd = algo(a, b)
    t2 = process_time() - t1

    # return algorithm name, iteration, time, and gcd
    return [str, i, t2, gcd]

# run algorithms multiple times with multiple values of a and b
def run_algos(algo, x, loops, str):
    results = []

    for i in range(x):

        # append algorithm name and start writing data with 1 instead of 0
        results.append([str, i + 1])

        for j in range(loops):

            # generate new values for a and b each time you loop through
            # new a and b values will have the same number of bits
            # i + 1 --> generate bits starting at 2^1 instead of 2^0
            a = generate_num(i + 1)
            b = generate_num(i + 1)

            # results[i].append(a)
            # results[i].append(b)

            t1 = process_time()
            gcd = algo(a, b)
            t2 = process_time() - t1

            # append gcd and running time
            # we should see a different gcd on each iteration
            # note: for larger values, odds are the gcd will be 1
            results[i].append(gcd)
            results[i].append(t2)

    return results

# function to generate random numbers based on increasing bits
def run_nums(x):
    numbers = []

    # for...in to evaluate numbers from 2 to x (use x+1 to include x)
    for i in range(2, x + 1):

        a = generate_num(i)
        b = generate_num(i)
        digits_a = len(str(abs(a)))
        digits_b = len(str(abs(b)))

        numbers.append([i, 2**i, digits_a, digits_b, a, b])

    return numbers

# run each algorithm with the same a and b values
def run_all(x):
    results = []

    # for...in to evaluate numbers from 2 to x (use x+1 to include x)
    for i in range(2, x + 1):

        a = generate_num(i)
        b = generate_num(i)

        if i < 5:
            res = time_algo(brute_force, i, a, b, "naive")
            results.append(res)

        res = time_algo(euclid_div, i, a, b, "euclid-div")
        results.append(res)

        res = time_algo(euclid_sub, i, a, b, "euclid-sub")
        results.append(res)

        if i < 16:
            res = time_algo(euclid_rec, i, a, b, "euclid-rec")
            results.append(res)

        res = time_algo(binary_gcd_loops, i, a, b, "binary-loops")
        results.append(res)

        if i < 14:
            res = time_algo(binary_gcd_rec, i, a, b, "binary-rec")
            results.append(res)

    return results

def main():

    # set number of bits for algorithms -- 2^x
    x = 21
    # set loops for run_algos()
    # I have used 5, 10, 20, and 100
    loops = 10

    numbers = run_nums(x)
    headers = ['iteration', 'bits', 'digits(a)', 'digits(b)', 'a', 'b']
    write_to_cvs('./data/test-1.csv', headers, numbers)

    results = run_all(x)
    headers = ['algorithm', 'bits (2^)', 'time', 'gcd']
    write_to_cvs('./data/test-2.csv', headers, results)

    # results = run_algos(brute_force, x, loops, "naive")
    # headers = ['algorithm', 'bits (2^)', 'gcd', 'times']
    # write_to_cvs('./data/test3-naive-10runs-2.csv', headers, results)


if __name__ == "__main__":
    main()