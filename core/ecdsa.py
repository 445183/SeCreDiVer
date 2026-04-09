from hashlib import sha256
import secrets
from core.ec import scalMul, pointAdd,G, n
from gmpy2 import f_mod,mul
from core.fieldArith import modinv

def genKeys():
    p=secrets.randbelow(n-1)+1
    return (p,scalMul(p,G))

def sign(m:bytes,d:int):
    k=secrets.randbelow(n-1)+1
    z=f_mod(int.from_bytes(sha256(m).digest(),'big'),n)
    r=scalMul(k,G)[0]
    s=f_mod(mul(modinv(k,n),z+mul(r,d)),n)
    return (r,s)

def verify(m:bytes,sgn:tuple,Q:tuple):
    z=f_mod(int.from_bytes(sha256(m).digest(),'big'),n)
    u1=f_mod(mul(modinv(sgn[1],n),z),n)
    u2=f_mod(mul(modinv(sgn[1],n),sgn[0]),n)
    return f_mod(pointAdd(scalMul(u1,G),scalMul(u2,Q))[0],n)==sgn[0]

def rsToDict(sgn:tuple):
    return {'r':format(sgn[0],'064x'),'s':format(sgn[1],'064x')}

def dictToRS(d:dict):
    return (int.from_bytes(bytes.fromhex(d['r']),'big'),int.from_bytes(bytes.fromhex(d['s']),'big'))