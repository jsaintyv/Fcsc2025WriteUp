from gmpy2 import powmod as pow
from Crypto.PublicKey import RSA

class Smolkkey:
	def __init__(self):
		k = RSA.generate(1024, e = 3)
		print(k)
		print(k.n)
		print(k.p)
		print(k.q)
		print(k.d)

		self.pk = (k.n, k.e)
		self.sk = (k.n, k.d)

	def encrypt(self, m):
		n, e = self.pk
		c = pow(m, e, n)
		return int(c)

	def decrypt(self, c):
		n, d = self.sk
		m = pow(c, d, n)
		return int(m)

# Generate a key
E = Smolkkey()


