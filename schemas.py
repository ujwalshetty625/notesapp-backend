from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel): #the request body that the user will send when they create an account
    name:str
    email:EmailStr
    password:str

class UserResponse(BaseModel): #the response users will get when they create an account or login from the app
    id:int
    name:str
    email:EmailStr

    class Config: #this is used to configure the pydantic model
        from_attributes = True #this is used to tell pydantic that the data will be coming from an ORM model and not from a dictionary

class NoteCreate(BaseModel):
    title:str
    content:str

class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    owner_id:int

    class Config:
        from_attributes=True