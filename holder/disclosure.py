from core.merkle import getProof,mkTree
def showCred(cred:dict[str,any],toShow:list[str]):
    shol=list()
    hid=dict()
    ht=mkTree([(cred['fields'][i]['name'],cred['fields'][i]['value']) for i in range(len(cred['fields']))])
    for i in range(len(cred['fields'])):
        if cred['fields'][i]['name'] in toShow:
            shol.append({
                'name':cred['fields'][i]['name'],
                'value':cred['fields'][i]['value'],
                'ftype':cred['fields'][i]['ftype'],
                'index':i,
                'proof':[[elem[0].hex(),elem[1]] for elem in getProof(ht,i)]
            })
        else:
            hid[cred['fields'][i]['name']]=ht[0][i].hex()

    return {
        'issuer_public_key':cred['issuer_public_key'],
        'root':cred['root'],
        'signature':cred['signature'],
        'issued_at':cred['issued_at'],
        'expires_at':cred['expires_at'],
        'revealed':shol,
        'hidden':hid
    }
