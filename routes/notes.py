from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Note,User
from schemas import NoteCreate,NoteResponse
from auth import get_current_user
from typing import List #this is used to specify the type of the response that the endpoint will return. In this case, it will return a list of NoteResponse objects.

router=APIRouter()

@router.post("/notes",response_model=NoteResponse)
def create_note(note:NoteCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    new_note=Note(title=note.title,content=note.content,owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note) #this is used to refresh the new_note object so that it has the id of the newly created note
    return new_note

@router.get("/notes",response_model=List[NoteResponse]) #this endpoint will return a list of notes that belong to the current user
def get_notes(db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    notes=db.query(Note).filter(Note.owner_id==current_user.id).all() #this will return all the notes that belong to the current user
    return notes

@router.get("/notes/{note_id}",response_model=NoteResponse)
def get_note(note_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    note=db.query(Note).filter(Note.id==note_id).first() #this will return the note with the given id
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    if note.owner_id!=current_user.id:
        raise HTTPException(status_code=403,detail="Not authorized to view this note")
    return note

@router.put("/notes/{note_id}",response_model=NoteResponse)
def update_note(note_id:int,updated_note:NoteCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    note=db.query(Note).filter(Note.id==note_id).first()
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    if note.owner_id!=current_user.id:
        raise HTTPException(status_code=403,detail="Not authorized to update this note")
    note.title=updated_note.title
    note.content=updated_note.content
    db.commit()
    db.refresh(note)
    return note

@router.delete("/notes/{note_id}")
def delete_note(note_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    note=db.query(Note).filter(Note.id==note_id).first()
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    if note.owner_id!=current_user.id:
        raise HTTPException(status_code=403,detail="Not authorized to delete this note")
    db.delete(note)
    db.commit()
    return {"message":"Note deleted successfully"}

