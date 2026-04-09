import json
import os
from pathlib import Path
p=Path('holder/wallet')

def save_cred(cred_dict:dict):
    with open(p/(cred_dict['cred_id']+'.json'),"w") as f:
        json.dump(cred_dict,f)

def load_cred(cred_id:str):
    file_name=p/(cred_id+'.json')
    if file_name in p.iterdir():
        with open(file_name,"r") as f:
            return json.load(f)
        
def list_cred():
    return [str(f.name).replace('.json','') for f in p.iterdir()]

def del_cred(cred_id:str):
    if p/(cred_id+'.json') in p.iterdir():
        os.remove(p/(cred_id+'.json'))