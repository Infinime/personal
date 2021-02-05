print("Primes less than?")
n = int(input())


def sieve(num):
    primes = []
    for x in range(2, num):
        if primes != []:
            if not dividecheckarr(x, primes):
                primes += [x]
        else:
            primes += [x]
    return primes


def dividecheckarr(num, arr):
    string = ""
    for x in arr:
        if num % x == 0:
            string += '1'
    return string != ''


print(sieve(n))
input()
