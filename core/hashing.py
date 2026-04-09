import hashlib

def hash_bytes(data:bytes):
    return hashlib.sha256(data).digest()

def hash_leaf(enc_byt:bytes):
    return hashlib.sha256(enc_byt).digest()

def hash_node(left:bytes,right:bytes):
    return hashlib.sha256(left+right).digest()