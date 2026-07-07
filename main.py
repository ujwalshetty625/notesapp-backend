from fastapi import FastAPI,Depends
from database import engine,Base
from routes import users
from auth import get_current_user
from models import User
from routes import notes

app=FastAPI()

app.include_router(users.router) #this will include the users router in the main app so that the endpoints defined in users.py can be accessed from the main app

@app.get("/me")
def get_me(current_user:User=Depends(get_current_user)):
    return {"email":current_user.email, "id":current_user.id}

app.include_router(notes.router)