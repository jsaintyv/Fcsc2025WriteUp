
# Bergere

[Il était une bergère](https://hackropole.fr/fr/challenges/misc/fcsc2025-misc-il-etait-une-bergere/) 


L'analyse du code montre qu'il faut calculer la racine carré d'un nombre *e*.
```python
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
```

Il faut donc implémenter la racine carré entière en assembleur.
C'est là qu'on comprend le nom de l'épreure car  il faut utiliser "Méthode de Héron" 


Algorithme : Méthode de Héron pour calculer √n
```python
def racine_entiere(n):
    if n < 2:
        return n
    gauche, droite = 1, n
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if milieu * milieu == n:
            return milieu
        elif milieu * milieu < n:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return droite  # Partie entière inférieure

# Exemple :
print(racine_entiere(10))  # Affiche 3 (car 3² ≤ 10 < 4²)

```

En assembleur, on obtient ce code. 

``` 
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
```

Une fois  le code compilé dans  le pseudo assembleur , on peut récupérer le flag:
FCSC{bdd5a8bcb20359f69f3999ba12c90e026c0961e441d0c6f1e23c952d51abc2b4}