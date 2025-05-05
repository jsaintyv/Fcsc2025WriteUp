# Python regular imports
import gmpy2
from Crypto.Util.number import getPrime
from random import randrange
import sys
# Public files (challenge specific)
from machine import Machine

sys.set_int_max_str_digits(8092)

def setup(bit_len):
    p = getPrime(bit_len)
    q = getPrime(bit_len)
    l = (p - 1) * (q - 1) // gmpy2.gcd(p - 1,q - 1)
    N = p*q
    return N, l

def solveProblem(k, N, M):
    T=pow(2, k)
    print(f"T={T}")
    R=pow(M, T, N)
    print(f"R={R}")
    return R

def test(code, k):
    N, l = setup(256)
    M = randrange(N)

    e = (1 << k) % l
    print(code)
    c = Machine(code, N = N)
    c.R5 = k
    c.R6 = M
    c.exponent = 2

    c.runCode()
    if c.error:
        print("error")
        return False

    if c.exponent != 2:
        print("exponent != 2")
        print(c.exponent)
        return False

    print(gmpy2.powmod(M, e, N))
    print(solveProblem(k, N, M))
    print(c.R6)
    

    if gmpy2.powmod(M, e, N) != c.R6:
        print("WRONG")

        return False

    return True

def correctness(code):
    print("[+] Testing correctness")

    if not test(code, 0):
        exit()


    
    if not test(code, (2 ** 3) | randrange(2 ** 3)):
        exit()

    '''
    if not test(code, (2 ** 13) | randrange(2 ** 13)):
        exit()
    '''

    return True

if __name__ == "__main__":

    print("Enter your bytecode in hexadecimal:")
    code = sys.argv[1]
    print(code)
    print("Length" + str(len(code)))
    
    
    if len(code) > 28:
       print("Too long " + str(len(code)))
       exit()
    
    if correctness(code):
        flag = open("flag.txt").read().strip()
        print(f"[+] Congrats! Here is the flag: {flag}")

