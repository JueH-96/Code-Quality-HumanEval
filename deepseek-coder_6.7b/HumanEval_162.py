import hashlib

def string_to_md5(text):
    if text == "":
        return None
    
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()