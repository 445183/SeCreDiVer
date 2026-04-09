from core.ec import xyFromb64
from core.ecdsa import dictToRS, verify
from datetime import datetime,timezone
from core.merkle import verifyProof
from issuer.revocation import isRev

def verifyDisc(disc:dict):
    q=xyFromb64(disc['issuer_public_key'])
    s=dictToRS(disc['signature'])
    r_hex=disc['root']
    r=bytes.fromhex(r_hex)
    if datetime.now(timezone.utc) > datetime.fromisoformat(disc['expires_at']):
        return (False, 'Credential has expired !')
    for d in disc['revealed']:
        pf=[(bytes.fromhex(n),side) for (n,side) in d['proof']]
        if not verifyProof(d['name'],d['value'],pf,r):
            return (False,'Invalid proof for consistency !')
    if not verify(r,s,q):
        return (False,'Not authenticated by the institution !')
    if isRev(r_hex):
        return (False,'The credentials have been revoked by the institution !')
    return (True,'Valid credentials !!')