start:      ; 
    MOV R0, RB             ; droite ~R0 = n
    MOV R2, #0x2
    CMP R0, R2
    JNCA exit
    MOV R1, #0x1           ; gauche ~R1 = 1
    MOV R5, #0x1    
WHILE_R0_GREATER_THAN_R1:  ; while gauche <= droite:
    CMP R0, R1
    JNCA exit
    ADD R3, R0, R1         
    DIV R3, R3, R2
    MUL R4, R3, R3
    CMP R4, RB
    JNZA ELIF1
    MOV R0, R3             
    JA exit

ELIF1:
    CMP R4, RB
    JCA ELIF2
    ADD R1, R3, R5
    JA WHILE_R0_GREATER_THAN_R1

ELIF2:
    SUB R0, R3, R5        
    JA WHILE_R0_GREATER_THAN_R1
    
exit:
    STP