# import modules
import random
from time import process_time
import csv
import sys
from gcd_euclid import euclid_div, euclid_sub, euclid_rec
from gcd_binary import binary_gcd_loops, binary_gcd_rec
from gcd_naive import brute_force

# find out current recursion limit
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)


# generate random number based on various input bit sizes
def generate_num(x):
    return random.getrandbits(2**x)


def write_to_cvs(outfile, x, times):
    with open(outfile, mode="wt", encoding="utf-8", newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['algorithm', 'bits (2^)', 'time', 'gcd'])

        for i in range(len(times)):
            writer.writerow(times[i])


def time_algo(algo, i, a, b, str):

    t1 = process_time()
    gcd = algo(a, b)
    t2 = process_time() - t1
    print(str, i, "time", t2, gcd)

    # return [str, i, t2, gcd, a, b]
    return [str, i, t2, gcd]

def run_algos(algo, x, loops, a, b, str):
    results = []

    for i in range(x):
        print("i", i)

        results.append([str, i+1, '2^' + str(i+1)])

        for j in range(loops):

            t1 = process_time()
            algo(a, b)
            t2 = process_time() - t1
            results[i].append(t2)
            print("x", i+1, j+1, "time", t2)

    print(results)
    return results

def main():
    results = []

    x = 19

    # for...in to evaluate numbers from 2 to x (use x+1 to include x
    for i in range(2, x+1):
        print(i)

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

        write_to_cvs('./data/test-all-19.csv', x, results)


if __name__ == "__main__":
    main()