import hashlib

def hash_bytes(data: bytes):
    """   Returns the raw 32-byte SHA-256 hash of any input.
          .digest() is used here to get raw binary instead of a hex string.
    
    Example: hash_bytes(b"IITR") -> b'\x8e\x... (32 bytes of binary)        """
    return hashlib.sha256(data).digest()

def hash_leaf(enc_byt: bytes):
    """     Turns a single credential field (like Name or GPA) into a hash.
            By hashing fields separately, we enable 'Selective Disclosure' later.
            Example: b'GPA:float:8.21' -> unique 32-byte leaf hash.               """
    return hashlib.sha256(enc_byt).digest()

def hash_node(left: bytes, right: bytes):
    """     Sticks two hashes together (+) and hashes the result. 
            This creates a link: if you change a child, the parent hash breaks.
            Logic: Parent = SHA256(Left_Hash + Right_Hash)  used to make node          """
    return hashlib.sha256(left + right).digest()