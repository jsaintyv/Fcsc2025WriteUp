# Python regular imports
from Crypto.Random.random import randrange
import sys
# Public files (challenge specific)
from machine import Machine

def test(code,e):
    c = Machine(code, e)
    c.runCode()
    if c.error:
        print("[!] Error!")
        exit()

    sqrt = c.R0
    if (e < sqrt ** 2) or (sqrt + 1) ** 2 <= e:
        print(f"[!] Error! {e} {sqrt}")
        exit()
    print("Success")

if __name__ == "__main__":
    
    print("Enter your bytecode in hexadecimal:")
    code = sys.argv[1]

    print("[+] Testing correctness...")
    test(code, 25)
    for _ in range(32):
        e = randrange(2 ** 4096)
        test(code, e)

    print("[+] Correct, congrats! Congrats! Here is the flag:")
    print(open("flag.txt").read().strip())

    
