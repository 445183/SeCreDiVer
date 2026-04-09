from core.hashing import hash_leaf,hash_node
from core.fieldEnc import encode_field

def mkTree(fp:list[tuple[str,any]]):
    tree=list()
    tree.append([])
    for i in range(len(fp)):
        tree[0].append(hash_leaf(encode_field(fp[i][0],fp[i][1])))
    while len(tree[-1])!=1:
        temp=list()
        for i in range(0,len(tree[-1]),2):
            if i!=len(tree[-1])-1:
                temp.append(hash_node(tree[-1][i],tree[-1][i+1]))
            else:
                temp.append(hash_node(tree[-1][i],tree[-1][i]))
        tree.append(temp)
    return tree

def getRoot(l:list[list[bytes]]):
    return l[-1][0]

def getProof(l:list[list[bytes]],ind:int):
    pftree=list()
    for i in range(len(l)-1):
        temp=tuple()
        if (ind&1)==0:
            temp=(l[i][ind+1 if ind+1<len(l[i]) else ind],'right')
        else:
            temp=(l[i][ind-1],'left')
        pftree.append(temp)
        ind//=2
    return pftree

def verifyProof(n:str,v:any,pf:list[tuple[bytes,str]],r):
    h=hash_leaf(encode_field(n,v))
    for i in range(len(pf)):
        if(pf[i][1]=='left'):
            h=hash_node(pf[i][0],h)
        else:
            h=hash_node(h,pf[i][0])
    return h==r

def bytToStr(tb:list[list[bytes]]):
    ts=list()
    for i in range(len(tb)):
        temp=list()
        for j in range(len(tb[i])):
            temp.append(tb[i][j].hex())
        ts.append(temp)
    return ts

def strToByt(ts:list[list[str]]):
    tb=list()
    for i in range(len(ts)):
        temp=list()
        for j in range(len(ts[i])):
            temp.append(bytes.fromhex(ts[i][j]))
        tb.append(temp)
    return tb