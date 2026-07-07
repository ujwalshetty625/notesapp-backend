from datetime import datetime, timedelta,timezone
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv() 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_db(): #used to get the database session for each request and close it after the request is done
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password) #returns True if the plain password matches the hashed password, else returns False

def create_access_token(data:dict):
    to_encode=data.copy() #create a copy of the data dictionary to encode it into a JWT token
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #set the expiration time for the token to be 30 minutes from the current time
    to_encode.update({"exp":expire}) #add the expiration time to the data dictionary
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) #encode the data dictionary into a JWT token using the secret key and the HS256 algorithm

Oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login") #this is used to get the token from the request header and verify it using the secret key and the HS256 algorithm

def get_current_user(token:str=Depends(Oauth2_scheme),db:Session=Depends(get_db)): #we define this once and use it in all routes that req JWT authentication. It will get the token from the request header and verify it using the secret key and the HS256 algorithm
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401,detail="Invalid Credentials")
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid Token")
    from models import User
    user=db.query(User).filter(User.email==email).first() #get the user from the database using the email from the token
    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    return user