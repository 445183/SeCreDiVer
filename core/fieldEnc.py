from datetime import datetime

def encode_field(name:str,value:str|int|float|bool|datetime):
    return (name+':'+type(value).__name__+':'+str(value)).encode('utf-8')