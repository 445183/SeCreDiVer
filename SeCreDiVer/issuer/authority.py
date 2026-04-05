from datetime import datetime, timezone, timedelta
from core.ecdsa import genKeys, sign, rsToDict
from core.ec import xyTob64
from core.merkle import mkTree, getRoot, bytToStr

class IssuerAuthority:
    def __init__(self,name:str):
        self.name=name
        kp=genKeys()
        self.priv_k=kp[0]
        self.publ_k=kp[1]

    def issueCred(self,holder:str,fields:dict[str,any],valDays:int):
        f_pairs=[(name,value) for name,value in fields.items()]
        cred=[{'name':name,'value':value,'ftype':type(value).__name__} for name,value in f_pairs]
        hash_tree=bytToStr(mkTree(f_pairs))
        
        root=getRoot(mkTree(f_pairs))
        sign_root=rsToDict(sign(root,self.priv_k))
        r_hex=root.hex()

        iss_tim=datetime.now(timezone.utc).isoformat()
        exp_tim=(datetime.now(timezone.utc)+timedelta(days=valDays)).isoformat()

        return {
            'cred_id':r_hex,
            'issuer':self.name,
            'holder':holder,
            'fields':cred,
            'levels':hash_tree,
            'root':r_hex,
            'signature':sign_root,
            'issued_at':iss_tim,
            'expires_at':exp_tim,
            'issuer_public_key':xyTob64(self.publ_k)
        }
    
    def getPubK(self):
        return xyTob64(self.publ_k)