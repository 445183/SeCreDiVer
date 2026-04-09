from secrets import randbelow
from gmpy2 import powmod

def modinv(a:int,p:int):
    return powmod(a,p-2,p)

def is_prime(m:int,k=20):
    if m<2:
        return False
    elif m==2:
        return True
    
    e,q=0,m-1
    while((q&1)==0):
        q//=2
        e+=1
    for i in range(k):
        r=randbelow(m-3)+2
        p=q
        while(p<m-1):
            if p==q and(powmod(r,p,m)==1 or powmod(r,p,m)==m-1):
                break
            elif powmod(r,p,m)==m-1:
                break
            else:
                p*=2
        if p==m-1:
            return False
    return True