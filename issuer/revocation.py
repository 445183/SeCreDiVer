from pathlib import Path
import json
rev_F=Path('issuer/revokInfo/revo_reg.json')

def revCred(r_hex:str):
    with open(rev_F,"r") as jf_r:
        d=json.load(jf_r)
    rl=list()
    if "revoked" in d:
        rl=d["revoked"]
    rl.append(r_hex)
    with open(rev_F,"w") as jf_w:
        json.dump({"revoked":rl},jf_w)

def isRev(r_hex:str):
    with open(rev_F,"r") as jf_r:
        d=json.load(jf_r)
    if "revoked" in d and r_hex in d["revoked"]:
        return True
    else:
        return False