from jose import jwt, JWTError
import rsa
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
from connexion.exceptions import ProblemException
def get_token(dictionary):
    # There are multiple ways to get secret keys, among which are:
    # OS Approach
    # import os
    # secret = os.urandom(14)

    # UUID Approach
    # import uuid
    # secret = uuid.uuid4().hex

    # Secrets [ only for Python 3.6 + ]
    # import secrets
    # secret =  secrets.token_urlsafe(14)
    dotenv_path = Path('./env')
    load_dotenv(dotenv_path=dotenv_path)
    JWT_SECRET = os.getenv(
        "TOKEN_SECURITY_KEY")  # YOUR SECRET KEY, We usually store it in a .env file and get it by os.getenv("JWT_SECRET")

    JWT_LIFETIME_SECONDS = 3600  # HOW LONG YOU WANT THE TOKEN TO STAY VALID BEFORE EXPIRING
    JWT_ALGORITHM = 'HS256'  # TYPE OF ALGORITHM TO ENCRYPT UR TOKEN, We usually store it in a .env file and get it by os.getenv("JWT_ALGORITHM")

    # we would usually get the following data from mongo db or our request.

    user_id = str(dictionary.get("_id",""))
    user_username = dictionary.get("username","")
    user_role = dictionary.get("role","")

    payload = {
        "iat": datetime.datetime.utcnow(),
        # THis variable is called Issued at Time, to let u know when the token was created
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_LIFETIME_SECONDS),
        # this is the expiry time, to let you know when the token expires, for us its in 3600 seconds in this example
        "id": user_id,  # A bunch of data we wanna quickly access later on.
        "username": user_username,  # A bunch of data we wanna quickly access later on.
        "role": user_role  # A bunch of data we wanna quickly access later on.
    }

    # ENCODING OUR DATA TO CREATE OUR TOKEN

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decode_token(token):
    JWT_SECRET = os.getenv("TOKEN_SECURITY_KEY")  # YOUR SECRET KEY, We usually store it in a .env file and get it by os.getenv("JWT_SECRET")
    JWT_ALGORITHM = 'HS256'  # TYPE OF ALGORITHM TO ENCRYPT UR TOKEN, We usually store it in a .env file and get it by os.getenv("JWT_ALGORITHM")
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        raise ProblemException(status=401,title="Unauthorized",detail="Token Invalid Or Expired.")


if __name__ == '__main__':
    token = get_token()
    print("token", token)
    token_data = decode_token(token)
    print("data", token_data)
