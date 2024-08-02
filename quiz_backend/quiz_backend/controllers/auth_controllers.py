from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from quiz_backend.settings import sec_key, algorithm

pwd_context = CryptContext(schemes="bcrypt")

def genereteToken(data:dict, expiry_time: timedelta):
    try:
        to_encode_data = data.copy()
        to_encode_data.update({
            "exp": expiry_time
        })
        access_token = jwt.encode(to_encode_data, sec_key, algorithm=algorithm)
        return access_token
    except JWTError as je:
        print(je)
    
def passwordIntoHash(plaintext:str):
    hashedpassword = pwd_context.hash(plaintext)
    return hashedpassword

