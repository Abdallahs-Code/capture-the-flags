from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes

n = 143991606075158483660871570161405209117
e = 65537
c = 34130411904650996210426832018051041635

print("[*] Factoring n...")

factors = factorint(n)
print("[+] Factors:", factors)

p, q = list(factors.keys())

# Compute phi
phi = (p - 1) * (q - 1)

# Compute d
d = inverse(e, phi)

# Decrypt
m = pow(c, d, n)

try:
    plaintext = long_to_bytes(m)
    print("[+] Plaintext:", plaintext.decode())
except:
    print("[+] Raw:", m)
