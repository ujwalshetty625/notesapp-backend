from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True) #index=True means that the column will be indexed for faster search when the db has a lot of data
    name=Column(String,nullable=False) #nullable=False means that the column cannot be empty or contain null values
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    notes=relationship("Note",back_populates="owner") #back_populates is used to define the relationship between the two tables so that we can access the notes of a user and the owner of a note easily. It is used in both classes to establish a bidirectional relationship.

class Note(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    owner=relationship("User",back_populates="notes") #back_populates is used to define the relationship between the two tables so that we can access the notes of a user and the owner of a note easily. It is used in both classes to establish a bidirectional relationship.