from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate,UserResponse
from passlib.context import CryptContext #used for hashing the password instead of storing it in plain text
from fastapi.security import OAuth2PasswordRequestForm
from auth import verify_password,create_access_token

router=APIRouter()
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") #this is used to hash the password using the bcrypt algorithm

def get_db(): #used to get the database session for each request and close it after the request is done
    db=SessionLocal()
    try:
        yield db #when the function is called, it will return the db session and then close it after the request is done
    finally:
        db.close()

@router.post("/signup",response_model=UserResponse) #the endpoint for creating a new user account it will take the request body as a UserCreate model and return a UserResponse model
def signup(user:UserCreate,db:Session=Depends(get_db)): 
    existing=db.query(User).filter(User.email==user.email).first() #check if the user already exists in the database by querying the User table and filtering by 
    if existing:
        raise HTTPException(status_code=400,detail="Email already registered") 
    hashed = pwd_context.hash(user.password) #else hash the password using the bcrypt algorithm and store it in the database
    new_user=User(name=user.name,email=user.email,password=hashed) 
    db.add(new_user)
    db.commit() #commit the changes to the database
    db.refresh(new_user) #refresh the new_user object to get the id of the newly created user
    return new_user

@router.post("/login") #the endpoint for logging in a user it will take the request body as a OAuth2PasswordRequestForm model and return a JWT token
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.email==form_data.username).first() #check if the user exists in the database by querying the User table and filtering by email
    if not user or not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=400,detail="Invalid Credentials")
    token=create_access_token(data={"sub":user.email}) #create a JWT token using the user's email as the subject
    return {"access_token":token,"token_type":"bearer"} #return the JWT token and the token type as bearer