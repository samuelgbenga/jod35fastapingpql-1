import logging
import uuid
from passlib.context import CryptContext 
from datetime import datetime, timedelta

import jwt

from src.config.loadenv import Config


def create_access_token(user_data: dict , expiry:timedelta = None, refresh: bool= False) -> str: # type: ignore
    payload = {
        'user':user_data,
        'exp': datetime.now() + (expiry if expiry is not None else timedelta(minutes=60)),
        'jti': str(uuid.uuid4()),
        'refresh' : refresh
    }


    token = jwt.encode(
        payload=payload,
        key= Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )

    return token

def decode_token(token: str) :
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )
        if token_data:
            return True
        else:
            return False
        
    except jwt.PyJWTError as jwte:
        logging.exception(jwte)
        print(token)
        return False
    
    except Exception as e:
        logging.exception(e)
        return False