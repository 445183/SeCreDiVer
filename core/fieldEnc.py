from datetime import datetime

def encode_field(name: str, value: str | int | float | bool | datetime):
    """    Standardizes data into a 'Label:Type:Value' format.
           Example: encode_field("GPA", 8.21) -> b'GPA:float:8.21'    """
    # 1. Format: Combines everything into one unique string
    data_string = name + ':' + type(value).__name__ + ':' + str(value)
    
    # 2. Encode: Converts text to bytes for the SHA-256 line:  
    #     hashlib.sha256(data).digest()  as sha256 takes data in bytes
    return data_string.encode('utf-8')