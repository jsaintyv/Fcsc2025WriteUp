# Smölkkey 

[Smölkkey](https://hackropole.fr/fr/challenges/crypto/fcsc2025-crypto-smolkkey/) 

Cet intro traite de l'algorithme RSA.


# Le chiffrement RSA
Le chiffrement RSA (Rivest-Shamir-Adleman) est un algorithme de cryptographie asymétrique largement utilisé pour sécuriser les communications.
RSA utilise une paire de clés : une clé publique pour le chiffrement et une clé privée pour le déchiffrement. La sécurité de RSA repose sur la difficulté de factoriser de grands nombres entiers.
Génération des clés

    Choix de deux nombres premiers distincts : p et q.
    Calcul du module : n=p×q
    Calcul de la fonction d'Euler : ϕ(n)=(p−1)×(q−1)
    Choix de l'exposant public : e tel que 1<e<ϕ(n) et e est premier avec ϕ(n).
    Calcul de l'exposant privé : d tel que d×e≡1mod  ϕ(n)d×e≡1modϕ(n).

La clé publique est le couple (n,e) et la clé privée est le couple (n,d).

*Chiffrement*
Pour chiffrer un message mm (où mm est un entier tel que 0≤m<n0≤m<n) :
c=(m^e) %  n

*Déchiffrement*
Pour déchiffrer le texte chiffré cc :
m=(c^d) % n


# Analyse du code smolkkey.py

Smolkkey utilise un *e* qui est 3 avec un n très grand 2048 bits

Résultat ,si le message est très petit  et que m^3  est inférieur à n, il est très simple de retrouver le message chiffré à partir de c.


```python
import gmpy2
from gmpy2 import powmod as pow
from Crypto.PublicKey import RSA

'''
Le message est trop court par rapport à la clé
Résultat  , on peut utiliser la racine cubique de C pour retrouver M
m=c^1/3
​
'''
c=6317668510138686569655374990729607736156413707292408158720036346854309670467296052918552527575331589363290061240725095262980389263184520673983411112154423282089471021996509038472493779143273789325774414352608726252566350689111876373836913240644190951995980896093509379920452743478551321978067299216590452459233562642920123055978471365092000347562228787318105538018723376505390423730687522026043802357456368003656219942603097205774742385485995835519133581552096067468551713114231926639878045212204590071768
racine_cubique, exact = gmpy2.iroot(c, 3)
taille_en_octets = (racine_cubique.bit_length() + 7) // 8
print(racine_cubique.to_bytes(taille_en_octets, byteorder='little'))
```


FCSC{30f7c4b2fa7f0fb48bfbd9bbd413491c0a6da660764961b862fe38a83b4bc00f}


