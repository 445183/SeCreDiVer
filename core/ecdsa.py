from hashlib import sha256
import secrets
from core.ec import scalMul, pointAdd, G, n
from gmpy2 import f_mod, mul
from core.fieldArith import modinv

def genKeys():
    """     Generates a random private Key (p) and calculates the Public Key (Q).
        Q = p * G (The starting point on the curve).    """
    p = secrets.randbelow(n-1) + 1  # secrets.randbelow is used for randomness which is cryptographically more secure.
    return (p, scalMul(p, G))

def sign(m: bytes, d: int):
    """   Signs a message m (usually the Merkle Root) using a Private Key d.
    Returns a signature (r, s).
    """
# 1. k is a nonce (a random number used only once). 
# If k is ever reused, the private key can be stolen  but it practically never happens 
    k = secrets.randbelow(n-1) + 1
# 2. Turn the message hash into a integer z
    z = f_mod(int.from_bytes(sha256(m).digest(), 'big'), n)

    r = scalMul(k, G)[0]  # 3. r is the x-coordinate of the point k*G
# 4. s = k⁻¹ * (z + r*d) mod n
    s = f_mod(mul(modinv(k, n), z + mul(r, d)), n)
    
    return (r, s)

def verify(m: bytes, sgn: tuple, Q: tuple):
    """  Checks if a signature (r, s) is valid for message m using Public Key Q.    """

    # 1. Get the message hash as an integer
    z = f_mod(int.from_bytes(sha256(m).digest(), 'big'), n)
    
    # 2. Math steps to reconstruct the signature point
    # u1 = z/s and u2 = r/s
    u1 = f_mod(mul(modinv(sgn[1], n), z), n)
    u2 = f_mod(mul(modinv(sgn[1], n), sgn[0]), n)
    
    # 3. Reconstruct the point: P = u1*G + u2*Q
    # If the signature is real, the x-coordinate of P will match r.
    return f_mod(pointAdd(scalMul(u1, G), scalMul(u2, Q))[0], n) == sgn[0]

def rsToDict(sgn: tuple):
    """Converts the signature (r, s) into a hex-dictionary for JSON storage."""
    return {'r': format(sgn[0], '064x'), 's': format(sgn[1], '064x')}

def dictToRS(d: dict):
    """Turns a hex-dictionary back into integer (r, s) for math verification."""
    return (int.from_bytes(bytes.fromhex(d['r']), 'big'), 
            int.from_bytes(bytes.fromhex(d['s']), 'big'))