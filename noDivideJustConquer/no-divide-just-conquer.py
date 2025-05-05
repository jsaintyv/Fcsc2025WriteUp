# Python regular imports
import gmpy2
import sys
import traceback
from Crypto.Random.random import randrange

# Public files (challenge specific)
from machine import Machine
from machine_restricted import RestrictedMachine, SuperRestrictedMachine

def testKey(p, q, iq, dp, dq, e, d, N, size):
    print(f"{p=}")
    print(f"{q=}")
    print(f"{iq=}")
    print(f"{dp=}")
    print(f"{dq=}")
    print(f"{e=}")
    print(f"{d=}")
    print(f"{N=}")
    if N != p * q:
        print(f"[!] Error! {N} is not {p * q}")
        return False

    if not gmpy2.is_prime(p):
        print(f"[!] Error! (p) {p}")
        return False

    if not gmpy2.is_prime(q):
        print(f"[!] Error! (q) {q}")
        return False
    
    if gmpy2.mod(q * iq, p) != 1:
        print("[!] Error! (iq)")
        return False

    if N.bit_length() != size:
        print(f"[!] Error! (N) {N}")
        return False

    m = randrange(N)
    if m != gmpy2.powmod(m, e * d, N):
        print("[!] Error! 33")
        return False

    if 0 != gmpy2.mod(m - gmpy2.powmod(m, e * dp, p), p):
        print("[!] Error! 37 ")
        return False

    if 0 != gmpy2.mod(m - gmpy2.powmod(m, e * dq, q), q):
        print("[!] Error! 41")
        return False

    return True

def randomPrimeE():
    size = [2, 4, 16, 256]
    size = size[randrange(4)]
    return gmpy2.next_prime(randrange((1 << size) - 1)) | 1

'''

    p et q
    iq tel que q * iq = 1 mod p
    dp et dq, tels que e * dp = 1 mod (p - 1) et e * dq = 1 mod (q - 1)
    d tel que e * d = 1 mod phi(N)
    N = p * q, exactement de la taille en bits donnée en entrée.

'''

def correctness(code, machine):
    print("[+] Testing correctness...")

    primes = set()
    for _ in range(32):
        e = randomPrimeE()

        size = randrange(512, 1024 + 1, 32)
        print(f"{size} {e}")
        print(f"{size = }, {e = }")
        try:
            c = machine(code, e, 1 << (size - 1))
            c.runCode()
        except:            
            c.printState()
            print("[!] Exception")
            print(traceback.format_exc())
            exit()
        
        if c.error:
            c.printState()
            print("[!] Error! 74")
            exit()

        if e != c.RB:
            print("[!] Error! (e)")
            exit()

        p  = c.R6
        q  = c.R7
        iq = c.R8
        dp = c.R9
        dq = c.RA
        d  = c.exponent
        N  = c.module
        primes.add(p)
        primes.add(q)

        if not testKey(p, q, iq, dp, dq, e, d, N, size):
            exit()

    if len(primes) != 1 << 6:
        exit()

    print("[+] Correct!")

def easy(code):
    correctness(code, Machine)
    flag_easy = open("flag_easy.txt").read().strip()
    print(f"[+] Congrats! Here is the easy flag: {flag_easy}")

def medium(code):
    correctness(code, RestrictedMachine)
    flag_medium = open("flag_medium.txt").read().strip()
    print(f"[+] Congrats! Here is the medium flag: {flag_medium}")

def hard(code):
    correctness(code, SuperRestrictedMachine)
    flag_hard = open("flag_hard.txt").read().strip()
    print(f"[+] Congrats! Here is the hard flag: {flag_hard}")

if __name__ == "__main__":
    print("Enter your bytecode in hexadecimal:")
    code = sys.argv[1]
    
    easy(code)        

    
