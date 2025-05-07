# No Divide Just Conquer 1/3

[No Divide Just Conquer 1/3](https://hackropole.fr/fr/challenges/hardware/fcsc2025-hardware-no-divide-just-conquer-1/) 


# Description

This first test simply consists of initializing an RSA key pair in assembler in order to satisfy the tests. We ask to generate the following values:

``` 
    p et q

    iq tel que q * iq = 1 mod p

    dp et dq, tels que e * dp = 1 mod (p - 1) et e * dq = 1 mod (q - 1)

    d tel que e * d = 1 mod phi(N)

    N = p * q, exactement de la taille en bits donnée en entrée.
```

The virtual machine is initialized with a public exponent and a size in bits.


# Analysis & implementation

The algorithm below is naive & non-optimal.

I determine p starting from a random number, I find the first prime number by incrementing by 1.

I deduce a q with q = n / p and then increment q until I find another valid prime number.

I check n = p*q to be the number of bits expected by n

Then I run the algorithm making sure that gcd(p-1, e) == 1 otherwise I take another pair of prime numbers.

# Solution

```
; RB = e    , RD = n 
start:      
    MOV R0, RD
    MOV R1, #0x1
retryPrimary:
    MOV R2, #0x5    
; R6 = p
    BTL R6, R0
    DIV R6, R6, R2
    RND R6
selectP1:
    ADD R6, R6, R1
    MR R6
    JNZR selectP1

; R7 = q
    DIV R7, R0, R6
selectP2:
    ADD R7, R7, R1
    MR R7
    JNZR selectP2

; R2 = N
    MUL R2, R6, R7
    BTL R4, R0
    BTL R5, R2
    CMP R4, R5 
    JNZA retryPrimary

; R4 = iq, RD = R6 = p    
    MOV RD, R6
    INV R4, R7        
     
; R8 = iq (no need to keep R4)    
    MOV R8, R4

; R3 = P-1 , R4 = Q-1    
    SUB R3, R6, R1        
    SUB R4, R7, R1    
; RD = PHI
    MUL R4, R3, R4
    MOV RD, R4
    MOV R3, RB    
; R3 = D = RC
    GCD R5, R3, R4
    CMP R5, R1
    JNZA retryPrimary
    INV R3, R3    
    MOV RC, R3
    
; R4 = P-1 ; 
    MOV R4, R6
    SUB R4, R4, R1    

; DP = D MOD (p-1)       
    MOV RD, R4
    MOV R4, RC
    MOD R4, R4
    MOV R9, R4

; R4 = Q-1 ; 
    MOV R4, R7
    SUB R4, R4, R1    

; DQ = D MOD (p-1)       
    MOV RD, R4
    MOV R4, RC
    MOD R4, R4
    MOV RA, R4

    MOV RD, R2

exit:
    STP
```