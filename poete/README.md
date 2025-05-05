# Poète

[Subject](https://hackropole.fr/fr/challenges/hardware/fcsc2025-hardware-proof-of-elapsed-time/)

The purpose of this test is to assess the ability to code in pseudo-assembly. The difficulty of the test lies in imposing a maximum size for the machine code.

We need to do for k, N, M 

```
e = (1 << k) % l
gmpy2.powmod(M, e, N)
```


Solution.asm solve the problem
```
start:      ; 51b10650C70303664c6dCFFA1400
    DIV      R1, R6, R6 
    CMP      R0, R5    
    JZR      exit
    POW      R6, R6
    SUB      R5, R5, R1   
    JR       start
exit:
    STP
```

The first trick is in  *DIV R1, R6, R6* which allow to avoid *MOV R1, #0x0001* which use 6 octet

*DIV R1, R6, R6*

51b1

*MOV R1, #0x0001*

80010000

The second trick compute *e = (1 << k) % l* required too much machine code. So we need to simplify it with a loop

M^(2^k) 

In  case, we hae : 

M = 5 

k = 3

2 ^ 3 => 8

M^8=>(((M^2)^2)^2)


In python, RC was initiailized at 2  (c.exponent = 2)

So , we loop k time on

POW      R6, R6

which equivalent to do

R6 = R6 ^ RC


To use less engine code, we use relative jump JZR, JR
