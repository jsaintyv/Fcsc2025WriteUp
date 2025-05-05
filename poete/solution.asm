start:      ; 51b10650C70303664c6dCFFA1400
    DIV      R1, R6, R6 
    CMP      R0, R5    
    JZR      exit
    POW      R6, R6
    SUB      R5, R5, R1   
    JR       start
exit:
    STP