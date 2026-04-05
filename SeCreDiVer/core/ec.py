from core.fieldArith import modinv
from gmpy2 import f_mod,mul
from base64 import urlsafe_b64encode as enc64
from base64 import urlsafe_b64decode as dec64

P=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
b=7
x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G=(x,y)
n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def pointAdd(p:tuple,q:tuple):
    if p==None:
        return q
    if q==None:
        return p
    lam=0
    if p[0]==q[0]:
        if p[1]!=q[1]:
            return None
        lam=f_mod((3*mul(p[0],p[0]))*modinv(2*p[1],P),P)
    else:
        lam=f_mod((q[1]-p[1])*modinv(q[0]-p[0],P),P)
    x=f_mod(mul(lam,lam)-p[0]-q[0],P)
    y=f_mod(mul(lam,p[0]-x)-p[1],P)
    return (x,y)

def scalMul(k:int,p:tuple):
    result=None
    binSum=p
    while(k>0):
        if((k&1)==1):
            result=pointAdd(binSum,result)
        binSum=pointAdd(binSum,binSum)
        k>>=1
    return result

def onCurv(p:tuple):
    return f_mod(mul(p[1],p[1])-mul(mul(p[0],p[0]),p[0])-b,P)==0

def xyTob64(p:tuple):
    return str(enc64(p[0].to_bytes(32,'big')+p[1].to_bytes(32,'big')).decode('utf-8'))

def xyFromb64(raw:str):
    raw=dec64(raw)
    return (int.from_bytes(raw[:32],'big'),int.from_bytes(raw[32:],'big'))